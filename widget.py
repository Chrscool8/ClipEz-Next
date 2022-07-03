# This Python file uses the following encoding: utf-8
import json
import os
import sys
from pathlib import Path
import glob
import re
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


def setdarkmode(enabled):
    if enabled:
        app.setStyleSheet(qdarkstyle.load_stylesheet())
    else:
        app.setStyleSheet("")


class MainWindow(QMainWindow):
    window = None
    app = None

    def __init__(self, _app):
        super(MainWindow, self).__init__()
        self.app = _app

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

        # self.setWindowTitle("ClipEZ-Next")
        app.setWindowIcon(QIcon('WackyScissorsOutline.png'))

        self.window.findChild(QAction, "action_exit").triggered.connect(quit)
        self.window.findChild(QAction, "action_theme").triggered.connect(setdarkmode)

        self.window.findChild(QPushButton, "button_cleartext").clicked.connect(self.clear_url)
        self.window.findChild(QPushButton, "button_getinfo").clicked.connect(self.get_video_info)
        self.window.findChild(QPushButton, "button_downloadstart").clicked.connect(self.click_download)
        self.window.findChild(QLineEdit, "lineedit_url").returnPressed.connect(self.click_download)
        self.window.findChild(QLineEdit, "lineedit_url").textChanged.connect(self.enable_clear_text_button)

        #widget_by_name(self.window, "image_thumb").setMinimumWidth(widget_by_name("treeview_detailed").height()*9/16)
        #widget_by_name(self.window, "image_thumb").setMaximumWidth(widget_by_name("treeview_detailed").height()*9/16)
        #widget_by_name(self.window, "image_thumb").setFixedWidth(self.widget_by_name("treeview_detailed").height()*9/16)

        self.enable_clear_text_button()

        self.clear_temps()

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
                ["Title", info_dict.get("title", None)],
                ["Uploader", info_dict.get("uploader", None)],
                ["ID", info_dict.get("id", None)],
                ["URL", info_dict.get("webpage_url", None)],
                ["Thumbnail", info_dict.get("thumbnail", None)],
                ["View Count", info_dict.get("view_count", None)],
                ["Duration", info_dict.get("duration", None)],
                ["Upload Date", info_dict.get("upload_date", None)],
                ["Age Limit", info_dict.get("age_limit", None)],
                ["Uploader ID", info_dict.get("uploader_id", None)],
                ["Uploader Url", info_dict.get("uploader_url", None)],
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
            self.window.findChild(QTextEdit, "textbox_status").append(
                styletext("b", colortext("Red", "ERROR: ")) + "Unsupported URL: "+styletext("i", url_text))

        self.app.processEvents()

    def clear_temps(self):
        files = glob.glob(os.getcwd()+"/temp/downloaded.*")
        for file in files:
            os.remove(file)

    def escape_ansi(self, line):
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        return ansi_escape.sub('', line)

    def my_hook(self, d):
        if d['status'] == 'finished':
            print('\n\nDone downloading.\n')
            self.window.findChild(QTextEdit, "textbox_status").append(styletext("b", colortext("Green", "DOWNLOAD: \t"))+"Done downloading.")

        if d['status'] == 'error':
            print('\n\nSomething went wrong with the download.\n')
            self.window.findChild(QTextEdit, "textbox_status").append(
                styletext("b", colortext("Green", "DOWNLOAD: \t"))+"Something went wrong with the download.")

        if d['status'] == 'downloading':
            self.window.findChild(QProgressBar, "progressbar_download").setValue(float(self.escape_ansi(d['_percent_str']).strip().replace("%", "")))

            status_line = styletext("b", colortext("Green", "DOWNLOAD: \t"))
            status_line += colortext("Blue", self.escape_ansi(d['_percent_str']))
            status_line += " of "
            status_line += styletext("i", colortext("Green", self.escape_ansi(d['filename'])))
            status_line += " ETA "
            status_line += colortext("Orange", self.escape_ansi(d['_eta_str']))
            self.window.findChild(QTextEdit, "textbox_status").append(status_line)

            self.app.processEvents()
            print(d['filename'], d['_percent_str'], d['_eta_str'])

    def click_download(self):
        self.get_video_info()

        try:
            os.makedirs(os.getcwd()+"/temp/")
        except:  # all good
            a = 0

        if (not os.path.isdir(os.getcwd()+"/temp/")):
            print("Can't find temp directory. Returning.")
            return False

        self.clear_temps()

        options = {
            'outtmpl': os.getcwd()+"/temp/downloaded.%(ext)s",
            'fixup': "detect_or_warn",
            'noplaylist': True,
            'progress_hooks': [self.my_hook],
        }

        ydl = yt_dlp.YoutubeDL(options)
        url_text = self.window.findChild(QLineEdit, "lineedit_url").text()
        info_dict = ydl.extract_info(url=url_text, download=True)

    def enable_clear_text_button(self):
        whether = (len(self.window.findChild(QLineEdit, "lineedit_url").text()) != 0)
        self.window.findChild(QPushButton,  "button_cleartext").setEnabled(whether)
        self.window.findChild(QPushButton, "button_getinfo").setEnabled(whether)
        self.window.findChild(QPushButton, "button_downloadstart").setEnabled(whether)

    def clear_url(self):
        self.window.findChild(QLineEdit, "lineedit_url").clear()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow(app)
    sys.exit(app.exec())
