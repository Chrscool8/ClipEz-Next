# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

 
#from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# Greetings
#@Slot()

import yt_dlp

class Widget(QWidget):
    
    def widget_by_name(self, name):
        return self.findChildren(QWidget, name)[0]
    
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def click_download(self):
        print("Button clicked, Hello!")
        ydl = yt_dlp.YoutubeDL({})
        info_dict = ydl.extract_info(url=self.widget_by_name("lineedit_url").text(), download=False)
        print(info_dict)

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        
        self.widget_by_name("button_downloadstart").clicked.connect(self.click_download)


        

        
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
