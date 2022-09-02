from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Task(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add new task")
        self.setFixedWidth(500)
        self.setFixedHeight(200)
        self.task_text = QLabel()
        self.task_text.setText("Insert new task")

        self.task_value = QLineEdit()
        self.task_value.resize(80, 5)
        self.task_value.move(15, 20)
        self.task_value.insert("")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_value)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.task_text, 0, 0)
        self.vbox.addWidget(self.task_value, 0, 1)
        self.vbox.addWidget(self.btn, 0, 2)

    def send_value(self):
        self.submitted.emit(
            self.task_value.text()
        )
        self.close()

class Update(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Update task")
        self.setFixedWidth(500)
        self.setFixedHeight(200)
        self.task_text = QLabel()
        self.task_text.setText("Updated task text")

        self.task_value = QLineEdit()
        self.task_value.resize(80, 5)
        self.task_value.move(15, 20)
        self.task_value.insert(text)

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.send_value)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.task_text, 0, 0)
        self.vbox.addWidget(self.task_value, 0, 1)
        self.vbox.addWidget(self.btn, 0, 2)

    def send_value(self):
        self.submitted.emit(
            self.task_value.text()
        )
        self.close()