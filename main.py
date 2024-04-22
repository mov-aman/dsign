import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QPainter, QPen, QPainterPath
from PyQt5.QtCore import Qt

class SignaturePad(QWidget):
    def __init__(self):
        super().__init__()
        self.path = QPainterPath()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.drawPath(self.path)

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        self.update()

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def clear(self):
        self.path = QPainterPath()
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.signature_pad = SignaturePad()
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.signature_pad.clear)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_signature)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.signature_pad)
        main_layout.addWidget(clear_button)
        main_layout.addWidget(save_button)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        self.setWindowTitle('E-Signature App')
        self.setGeometry(300, 300, 600, 500)

    def save_signature(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", os.getenv('HOME'), "PNG(*.png);;JPEG(*.jpg *.jpeg)")
        if file_path:
            pixmap = self.signature_pad.grab()
            pixmap.save(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
