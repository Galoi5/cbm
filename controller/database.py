import sqlite3
from datetime import datetime
from enum import IntEnum


class EntryAlreadyExists(Exception):
    pass

class CategoryDoesntExist(Exception):
    pass
    
class UpdateEnum(IntEnum):
    TITLE = 1
    CATEGORIES = 2
    DATA = 3 

class Database():
    def __init__(self) -> None:
        self.con = sqlite3.connect("clipboardmanager.db")
        self.cur = self.con.cursor()

        with open("controller/tags.txt", "r") as f:
            self.data = f.readlines()

    def CreateTables(self):
        self.cur.execute("CREATE TABLE clipboard(title, category, date, data)")
    
    def AddClipboard(self, title: str, category: str, date: datetime, data: str):

        self.cur.execute("""
            INSERT INTO clipboard VALUES(?,?,?,?)
            """, (title, category, date, data))
        
        self.con.commit()

    def RemoveClipboard(self, title: str):
        self.cur.execute("DELETE from clipboard where title = ?", (title,))
        self.con.commit()

    def GetClipboards(self):
        self.cur.execute("SELECT * FROM clipboard")
        return self.cur.fetchall()
    
    def EditClipoard(self, what_to_edit: UpdateEnum, edit: str, title: str):
        if what_to_edit == UpdateEnum.TITLE:
            self.cur.execute("UPDATE clipboard SET title = ? WHERE title = ?", (edit,title))
            self.con.commit()
        elif what_to_edit == UpdateEnum.DATA:
            self.cur.execute("UPDATE clipboard SET data = ? WHERE title = ?", (edit,title))
            self.con.commit()
        elif what_to_edit == UpdateEnum.CATEGORIES:
            self.cur.execute("UPDATE clipboard SET category = ? WHERE title = ?", (edit,title))
            self.con.commit()

    def Close(self):
        self.cur.close()
        self.con.close()
