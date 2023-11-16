from PySide6.QtWidgets import (QDialog)


class SearchClipboard(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Search Clipboard")