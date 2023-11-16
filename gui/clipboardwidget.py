from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QGroupBox
from controller.database import Database
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtCore import (Qt, QCoreApplication, QSize, Slot)
import pyperclip
from gui.edit import EditClipboard

class ClipBoardWidget(QWidget):
    def __init__(self, title, date, categories, data) -> None:
        super().__init__()

        self.title = title
        self.db = Database()
        self.data = data

        self.cbwidget_layout = QHBoxLayout()
        self.title_label = QLabel(title)
        self.date_label = QLabel(date)
        self.categories_label = QLabel(categories)
        self.data_label = QLabel(self.data)
        self.edit_button = QPushButton(QIcon("gui/assets/edit.svg"), "")
        self.edit_button.clicked.connect(self.edit_cb)
        self.remove_button = QPushButton(QIcon("gui/assets/trash.svg"), "")
        self.remove_button.clicked.connect(self.remove_cb)
        self.copy_to_cb_button = QPushButton(QIcon("gui/assets/copy.svg"), "")
        self.copy_to_cb_button.clicked.connect(self.copy_cb)

        self.cbwidget_layout.addWidget(self.title_label)
        self.cbwidget_layout.addWidget(self.date_label)
        self.cbwidget_layout.addWidget(self.categories_label)
        self.cbwidget_layout.addWidget(self.data_label)
        self.cbwidget_layout.addWidget(self.edit_button)
        self.cbwidget_layout.addWidget(self.remove_button)
        self.cbwidget_layout.addWidget(self.copy_to_cb_button)
        
        self.setLayout(self.cbwidget_layout)
    
    @Slot()
    def edit_cb(self):
        global g1
        g1 = EditClipboard()
        g1.show()
    @Slot()
    def remove_cb(self):
        self.db.RemoveClipboard(self.title)
    @Slot()
    def copy_cb(self):
        pyperclip.copy(self.data)
    
        
        
