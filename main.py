import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from extends import *

class MainWindow(QWidget):  # Klasa MainWindow zawierająca główne okno programu

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TODO List")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        add_btn = QPushButton('Add')
        add_btn.clicked.connect(self.create_task)

        remove_btn = QPushButton('Remove')
        remove_btn.clicked.connect(self.remove_task)

        update_btn = QPushButton('Update')
        update_btn.clicked.connect(self.update_task)

        self.task_list = QListWidget()

        self.txt_file = open("tasks.txt", "r+")
        self.content_list = self.txt_file.read().split('\n')
        for item in self.content_list:
            self.task_list.addItem(item)


        grid = QGridLayout(self)
        grid.addWidget(add_btn, 0, 0, Qt.AlignTop | Qt.AlignLeft)
        grid.addWidget(update_btn, 0, 1, Qt.AlignTop | Qt.AlignCenter)
        grid.addWidget(remove_btn, 0, 2, Qt.AlignTop | Qt.AlignRight)
        grid.addWidget(self.task_list, 1, 0, Qt.AlignHCenter)

    def create_task(self):
        self.task = Task()
        self.task.submitted.connect(self.add_task)
        self.task.show()

    def remove_task(self):
        if self.task_list.currentItem() is None: return
        temp = self.task_list.selectedItems()
        self.content_list.remove(self.task_list.currentItem().text())
        for item in temp:
            self.task_list.takeItem(self.task_list.row(item))

    def update_task(self):
        if self.task_list.currentItem() is None: return
        self.update = Update(self.task_list.currentItem().text())
        self.update.submitted.connect(self.set_task)
        self.update.show()

    @pyqtSlot(str)
    def add_task(self, task):
        self.task_list.addItem(task)
        self.content_list.append(task)

    @pyqtSlot(str)
    def set_task(self, task):
        for i in range(len(self.content_list)):
            if self.content_list[i] == self.task_list.currentItem().text():
                self.content_list[i] = task
                break
        self.task_list.currentItem().setText(task)

    def closeEvent(self, QCloseEvent):
        self.txt_file.truncate(0)
        self.txt_file.write("\n".join(self.content_list))
        self.txt_file.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())

