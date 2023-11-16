from PySide6.QtWidgets import (QDialog, QLabel, QLineEdit, QPushButton, QGridLayout)
import datetime
from controller.database import Database
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtCore import (Qt, QCoreApplication, QSize, Slot)

class EditClipboard(QDialog):
    def __init__(self) -> None:

        super().__init__()

        self.db = Database()
        self.setWindowTitle("Add Clipboard")

        self.lay = QGridLayout()

        self.cb_name = QLabel("Name")
        self.cb_name_lineedit = QLineEdit()

        self.cb_data = QLabel("Data")
        self.cb_data_lineedit = QLineEdit()

        self.cb_categories = QLabel("Categories")
        self.cb_categories_lineedit = QLineEdit()

        self.seperator_info = QLabel("<i>Seperate categoris with ';'</i>")

        self.add_btn = QPushButton(QIcon("gui/assets/add.svg"), "Add")
        self.add_btn.clicked.connect(self.add_cb_to_db)

        self.lay.addWidget(self.cb_name, 0, 0)
        self.lay.addWidget(self.cb_name_lineedit, 0, 1)
        self.lay.addWidget(self.cb_data, 1, 0)
        self.lay.addWidget(self.cb_data_lineedit, 1, 1)
        self.lay.addWidget(self.cb_categories, 2, 0)
        self.lay.addWidget(self.cb_categories_lineedit, 2, 1)
        self.lay.addWidget(self.seperator_info, 3, 0 )
        self.lay.addWidget(self.add_btn,4,0,1,2)

        self.setLayout(self.lay)

    @Slot()
    def add_cb_to_db(self):
        title = self.cb_name_lineedit.text()
        categories = self.cb_categories_lineedit.text()
        date = datetime.datetime.now()
        data = self.cb_data.text()
        self.db.AddClipboard(title, categories, date, data)
        self.deleteLater()