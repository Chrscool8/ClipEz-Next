# This Python file uses the following encoding: utf-8
import json
import os
import sys
from pathlib import Path

import yt_dlp
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QWidget
from PySide6.examples.widgets.itemviews.jsonmodel import jsonmodel

import qdarkstyle


def colortext(color, text):
    styled_text = "<font color=\""+color+"\">"
    styled_text += text
    styled_text += "</font>"
    return styled_text


def styletext(stylecode, text):
    styled_text = "<"+stylecode+">"
    styled_text += text
    styled_text += "</"+stylecode+">"
    return styled_text


class Widget(QWidget):

    def widget_by_name(self, name):
        return self.findChildren(QWidget, name)[0]

    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        self.setWindowTitle("ClipEZ-Next")

    def click_download(self):
        self.widget_by_name("textbox_status").append(styletext("b", colortext("Green", "INFO: "))+"Getting Video Info...")
        ydl = yt_dlp.YoutubeDL({})
        url_text = self.widget_by_name("lineedit_url").text()
        try:
            info_dict = ydl.extract_info(url=url_text, download=False)
            document = json.loads(json.dumps(info_dict, indent=4))
            model = jsonmodel.JsonModel()
            model.load(document)
            self.widget_by_name("treeview_detailed").setModel(model)
            self.widget_by_name("textbox_status").append(styletext("b", colortext("Green", "INFO: ")) + "Got Video Info!")
        except Exception as e:
            print(e)
            self.widget_by_name("textbox_status").append(styletext("b", colortext("Red", "ERROR: ")) + "Unsupported URL: "+styletext("i", url_text))

    def enable_clear_text_button(self):
        whether = (len(self.widget_by_name("lineedit_url").text()) != 0)
        self.widget_by_name("button_cleartext").setEnabled(whether)
        self.widget_by_name("button_getinfo").setEnabled(whether)
        self.widget_by_name("button_downloadstart").setEnabled(whether)

    def clear_url(self):
        self.widget_by_name("lineedit_url").clear()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)

        self.widget_by_name("button_cleartext").clicked.connect(self.clear_url)
        self.widget_by_name("button_getinfo").clicked.connect(self.click_download)
        self.widget_by_name("lineedit_url").returnPressed.connect(self.click_download)
        self.widget_by_name("lineedit_url").textChanged.connect(self.enable_clear_text_button)

        self.enable_clear_text_button()

        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    widget = Widget()
    widget.show()
    sys.exit(app.exec())
