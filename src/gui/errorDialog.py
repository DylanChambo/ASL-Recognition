from PyQt6.QtWidgets import QWidget, QPushButton, QDialog, QLabel, QGridLayout
from PyQt6.QtCore import Qt


class ErrorDialog(QDialog):
    # Dialog to train the database
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Error")

        self.mainLayout = QGridLayout()

        self.errorLbl = QLabel("Error: Unable to find model")
        self.mainLayout.addWidget(
            self.errorLbl, 0, 0, 1, 0, Qt.AlignmentFlag.AlignCenter)
        self.okBtn = QPushButton("Ok")
        self.okBtn.clicked.connect(self.close)
        self.mainLayout.addWidget(
            self.okBtn, 1, 0, 1, 0, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.mainLayout)
        self.show()
