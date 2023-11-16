import json
from controller.database import Database
from gui.gui import GUI
import sys
from PySide6.QtWidgets import QApplication

class CBManager():
    def __init__(self) -> None:
        pass

    def _is_setup(self) -> bool:
        self._file = open("config.json")
        self._data = json.load(self._file)

        return self._data["setup"]
    
    def _setup(self) -> None:
        self.db = Database()
        self.db.CreateTables()
        self.db.Close()

        with open("config.json", "r") as json_file:
            data = json.load(json_file)

        data["setup"] = True

        with open("config.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    if CBManager()._is_setup():
        gui = GUI()
        gui.setFixedWidth(600)
        gui.setFixedHeight(400)
        gui.show()
    else:
        CBManager()._setup()
        gui = GUI()
        gui.setFixedWidth(600)
        gui.setFixedHeight(400)
        gui.show()

    sys.exit(app.exec())