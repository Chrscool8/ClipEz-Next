# This Python file uses the following encoding: utf-8
import json
import os
import sys
from pathlib import Path

import yt_dlp

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.examples.widgets.itemviews.jsonmodel import jsonmodel

import qdarkstyle
import urllib.request


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


def list_entry(json_data, title, tag):
    entry = ["", ""]

    entry[0] = title

    answer = json_data.get(tag, "N/A")
    #line_length = 50
    #list_lines = [answer[i:i+line_length] for i in range(0, len(answer), line_length)]

    # for line in list_lines:
    #    entry[1] += line + "\n"

    return answer


'''def widget_by_name(obj, name):
    results = obj.findChildren(QWidget, name)
    if len(results) > 0:
        return results[0]
    return QWidget()
'''


class MainWindow(QMainWindow):
    window = None

    def __init__(self):
        super(MainWindow, self).__init__()

        ui_file_name = "mainwindow.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()
        if not window:
            print(loader.errorString())
            sys.exit(-1)
        window.show()
        self.window = window

        self.setWindowTitle("ClipEZ-Next")


        self.window.findChild(QAction, "action_exit").triggered.connect(quit)

        self.window.findChild(QPushButton, "button_cleartext").clicked.connect(self.clear_url)
        self.window.findChild(QPushButton, "button_getinfo").clicked.connect(self.get_video_info)
        self.window.findChild(QPushButton, "button_downloadstart").clicked.connect(self.click_download)
        self.window.findChild(QLineEdit, "lineedit_url").returnPressed.connect(self.click_download)
        self.window.findChild(QLineEdit, "lineedit_url").textChanged.connect(self.enable_clear_text_button)

        #widget_by_name(self.window, "image_thumb").setMinimumWidth(widget_by_name("treeview_detailed").height()*9/16)
        #widget_by_name(self.window, "image_thumb").setMaximumWidth(widget_by_name("treeview_detailed").height()*9/16)
        #widget_by_name(self.window, "image_thumb").setFixedWidth(self.widget_by_name("treeview_detailed").height()*9/16)

        self.enable_clear_text_button()

    def get_video_info(self):
        self.window.findChild(QTextEdit, "textbox_status").append(styletext("b", colortext("Green", "INFO: "))+"Getting Video Info...")
        ydl = yt_dlp.YoutubeDL({})
        url_text = self.window.findChild(QLineEdit, "lineedit_url").text()
        try:
            info_dict = ydl.extract_info(url=url_text, download=False)
            json_data = json.dumps(info_dict, indent=4)
            print(info_dict)
            document = json.loads(json_data)
            model = jsonmodel.JsonModel()
            model.load(document)
            self.window.findChild(QTreeView, "treeview_detailed").setModel(model)
            self.window.findChild(QTextEdit, "textbox_status").append(styletext("b", colortext("Green", "INFO: ")) + "Got Video Info!")

            list_info = [
                ["title", info_dict.get("title", None)],
                ["uploader", info_dict.get("uploader", None)],
                ["id", info_dict.get("id", None)],
                ["webpage_url", info_dict.get("webpage_url", None)],
                ["thumbnail", info_dict.get("thumbnail", None)],
                ["view_count", info_dict.get("view_count", None)],
                ["duration", info_dict.get("duration", None)],
                ["upload_date", info_dict.get("upload_date", None)],
                ["age_limit", info_dict.get("age_limit", None)],
                ["uploader_id", info_dict.get("uploader_id", None)],
                ["uploader_url", info_dict.get("uploader_url", None)],
                ["Subscribers", info_dict.get("channel_follower_count", None)],
            ]

            for i in range(len(list_info)):
                self.window.findChild(QTableWidget, "table_simple").insertRow(self.window.findChild(QTableWidget, "table_simple").rowCount())
                self.window.findChild(QTableWidget, "table_simple").setItem(i, 0, QTableWidgetItem(list_info[i][0]))
                self.window.findChild(QTableWidget, "table_simple").setItem(i, 1, QTableWidgetItem(list_info[i][1]))

            thumb_url = info_dict.get("thumbnail", None)
            if thumb_url != None:
                with urllib.request.urlopen(thumb_url) as _url:
                    data = _url.read()
                    px = QPixmap()
                    px.loadFromData(data)
                    self.window.findChild(QLabel, "image_thumb").setPixmap(px)

        except Exception as e:
            print(e)
            self.window.findChild(QTextEdit,  "textbox_status").append(
                styletext("b", colortext("Red", "ERROR: ")) + "Unsupported URL: "+styletext("i", url_text))

    def click_download(self):
        self.get_video_info()

    def enable_clear_text_button(self):
        whether = (len(self.window.findChild(QLineEdit,  "lineedit_url").text()) != 0)
        self.window.findChild(QPushButton,  "button_cleartext").setEnabled(whether)
        self.window.findChild(QPushButton, "button_getinfo").setEnabled(whether)
        self.window.findChild(QPushButton, "button_downloadstart").setEnabled(whether)

    def clear_url(self):
        self.widget_by_name("lineedit_url").clear()


if __name__ == "__main__":
    app = QApplication([])
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    widget = MainWindow()
    sys.exit(app.exec())
