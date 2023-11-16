from PySide6.QtWidgets import (QMainWindow,
                               QToolBar,
                               QWidget,
                               QToolButton,
                               QVBoxLayout,
                               QScrollArea
                               )
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtCore import (Qt, QCoreApplication, QSize, Slot)
from controller.database import Database
from gui.add import AddClipboard
from gui.search import SearchClipboard
from gui.remove import RemoveClipboard
from gui.clipboardwidget import ClipBoardWidget

class GUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
 
        self.setWindowTitle("Clipboard Manager")

        self.tool_bar = QToolBar(self)
        self.tool_bar.setObjectName(u"toolBar")
        self.addToolBar(Qt.TopToolBarArea, self.tool_bar)
        self.tool_bar.setMovable(False)

        self.add_cb_btn = QToolButton()
        self.add_cb_btn.setIcon(QIcon("gui/assets/add.svg"))
        self.add_cb_btn.clicked.connect(self.addcbshow)

        self.remove_cb_btn = QToolButton()
        self.remove_cb_btn.setIcon(QIcon("gui/assets/trash.svg"))
        self.remove_cb_btn.clicked.connect(self.removecbshow)


        self.search_cb_btn = QToolButton()
        self.search_cb_btn.setIcon(QIcon("gui/assets/search.svg"))
        self.search_cb_btn.clicked.connect(self.searchcbshow)

        self.tool_bar.addWidget(self.add_cb_btn)
        self.tool_bar.addWidget(self.remove_cb_btn)
        self.tool_bar.addWidget(self.search_cb_btn)


        self.slate_layout = QVBoxLayout()
        self.scroll_cb = QScrollArea()
        self.slate = QWidget()
        self.db = Database()

        for u in self.db.GetClipboards():
            obj = ClipBoardWidget(u[0], u[2], u[1], u[3])
            self.slate_layout.addWidget(obj)
        
        self.slate_layout.setStretch(0,0)
        
        self.slate.setLayout(self.slate_layout)

        self.scroll_cb.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_cb.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_cb.setWidgetResizable(True)
        self.scroll_cb.setWidget(self.slate)
    
        self.setCentralWidget(self.scroll_cb)

    @Slot()
    def addcbshow(self):
        global g1
        g1 = AddClipboard()
        g1.show()

    
    @Slot()
    def removecbshow(self):
        global g2
        g2 = RemoveClipboard()
        g2.show()
    
    @Slot()
    def searchcbshow(self):
        global g3
        g3 = SearchClipboard()
        g3.show()