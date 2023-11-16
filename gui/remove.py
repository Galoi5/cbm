from PySide6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit, QGridLayout)
from PySide6.QtGui import QIcon
from controller.database import Database
from PySide6.QtCore import (Qt, QCoreApplication, QSize, Slot)


class RemoveClipboard(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Remove Clipboard")
        self.db = Database()
        self.setWindowTitle("Add Clipboard")

        self.lay = QGridLayout()

        self.remove_by_name = QLabel("Remove clipboard by name")
        self.remove_by_name_lineedit = QLineEdit()

        self.remove_cb_button = QPushButton(QIcon("gui/assets/trash.svg"), "Remove")
        self.remove_cb_button.clicked.connect(self.remove_cb_from_db)

        self.lay.addWidget(self.remove_by_name, 0, 0)
        self.lay.addWidget(self.remove_by_name_lineedit, 0, 1)
        self.lay.addWidget(self.remove_cb_button, 1,0 ,1, 2)
        
        self.setLayout(self.lay)

    @Slot()
    def remove_cb_from_db(self):
        self.db.RemoveClipboard(self.remove_by_name_lineedit.text())
        self.deleteLater()

    

      