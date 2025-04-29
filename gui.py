from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PySide6.QtCore import Qt, QThread, Signal, QSize
from PySide6.QtGui import QMovie
import sys
import subprocess

class DownloadThread(QThread):
    finished = Signal()
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        subprocess.run(["./yt-dlp", self.url])
        self.finished.emit()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Youtube Downloader')
        self.resize(800, 700)

        main_layout = QVBoxLayout()
        main_layout.addStretch(1)  # Top vertical stretch

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignHCenter)
        self.status_label.setStyleSheet("font-weight: bold; font-size: 18px;")
        main_layout.addWidget(self.status_label)

        # Centered group layout
        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignHCenter)  # Center horizontally

        self.label = QLabel("Enter URL Below")
        self.input = QLineEdit()
        self.input.setFixedWidth(600)

        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.on_submit)

        # Spinner setup
        self.spinner = QLabel()
        self.spinner.setAlignment(Qt.AlignHCenter)
        spinner_size = 48  # or any size you want
        self.spinner.setFixedSize(spinner_size, spinner_size)
        self.movie = QMovie("spinner.gif")
        self.movie.setScaledSize(QSize(spinner_size, spinner_size))
        self.spinner.setMovie(self.movie)
        self.spinner.hide()  # Hide by default

        center_layout.addWidget(self.label, alignment=Qt.AlignHCenter)
        center_layout.addWidget(self.input, alignment=Qt.AlignHCenter)
        center_layout.addWidget(self.button, alignment=Qt.AlignHCenter)
        center_layout.addWidget(self.spinner, alignment=Qt.AlignHCenter)

        main_layout.addLayout(center_layout)
        main_layout.addStretch(1)  # Bottom vertical stretch

        self.setLayout(main_layout)

    def on_submit(self):
        url = self.input.text()
        if url:
            self.status_label.setText("Downloading...")
            self.button.setEnabled(False)
            self.spinner.show()
            self.movie.start()
            self.thread = DownloadThread(url)
            self.thread.finished.connect(self.on_download_finished)
            self.thread.start()

    def on_download_finished(self):
        self.button.setEnabled(True)
        self.spinner.hide()
        self.movie.stop()
        self.status_label.setText("Download Complete!")

app = QApplication(sys.argv)

dark_stylesheet = """
QWidget {
    background-color: #232629;
    color: #F0F0F0;
}
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #2b2b2b;
    color: #F0F0F0;
    border: 1px solid #444;
    font-size: 18pt;
}
QPushButton {
    background-color: #444;
    color: #F0F0F0;
    border: 1px solid #666;
    padding: 5px;
    border-radius: 4px;
}
QPushButton:hover {
    background-color: #555;
}
QLabel {
    color: #F0F0F0;
    font-size: 20pt;
}
QProgressBar {
    background-color: #2b2b2b;
    color: #F0F0F0;
    border: 1px solid #444;
}
"""
app.setStyleSheet(dark_stylesheet)

window = MyWidget()
window.show()
sys.exit(app.exec())
