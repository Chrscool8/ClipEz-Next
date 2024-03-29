# This Python file uses the following encoding: utf-8
from asyncio.windows_events import NULL
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


def browse_for_file(destination_widget: QLineEdit):
    filename = QFileDialog.getOpenFileName(caption="Open Video", dir=os.getcwd(), filter="Video File (*.*)")
    if destination_widget != NULL:
        destination_widget.setText(filename[0])
    return filename[0]


def text_color(color, text):
    styled_text = "<font color=\""+color+"\">"
    styled_text += text
    styled_text += "</font>"
    return styled_text


def text_style(stylecode, text):
    styled_text = "<"+stylecode+">"
    styled_text += text
    styled_text += "</"+stylecode+">"
    return styled_text


def setdarkmode(enabled):
    if enabled:
        app.setStyleSheet(qdarkstyle.load_stylesheet())
    else:
        app.setStyleSheet("")


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        self.to_screen('Doing stuff')
        return [], info


class MainWindow(QMainWindow):
    window = None
    app = None
    save_video_location = os.getcwd() + "/temp/download"

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

        app.setWindowIcon(QIcon('WackyScissorsOutline.png'))

        self.window.findChild(QAction, "action_exit").triggered.connect(quit)
        self.window.findChild(QAction, "action_theme").triggered.connect(setdarkmode)

        self.window.findChild(QPushButton, "button_cleartext").clicked.connect(self.clear_url)
        self.window.findChild(QPushButton, "button_getinfo").clicked.connect(self.get_video_info)
        self.window.findChild(QPushButton, "button_downloadstart").clicked.connect(self.click_download)
        self.window.findChild(QLineEdit, "lineedit_url").returnPressed.connect(self.click_download)
        self.window.findChild(QLineEdit, "lineedit_url").textChanged.connect(self.enable_clear_text_button)

        self.window.findChild(QPushButton, "button_resultingfile").clicked.connect(self.click_location_butlab)

        self.window.findChild(QPushButton, "button_browsevideo").clicked.connect(
            lambda: browse_for_file(self.window.findChild(QLineEdit, "lineedit_videopath")))

        #widget_by_name(self.window, "image_thumb").setMinimumWidth(widget_by_name("treeview_detailed").height()*9/16)
        #widget_by_name(self.window, "image_thumb").setMaximumWidth(widget_by_name("treeview_detailed").height()*9/16)
        #widget_by_name(self.window, "image_thumb").setFixedWidth(self.widget_by_name("treeview_detailed").height()*9/16)

        self.enable_clear_text_button()

        self.clear_temps()

    def click_location_butlab(self):
        folder_loc = os.getcwd()+"/temp/"
        folder_loc = folder_loc.replace("/", "\\")
        print(folder_loc)
        if os.path.isdir(folder_loc):
            #subprocess.Popen(r'explorer /select,"'+folder_loc+'"')
            os.startfile(folder_loc)

    def get_video_info(self):
        self.window.findChild(QTextEdit, "textbox_status").append(text_style("b", text_color("Green", "INFO: "))+"Getting Video Info...")
        ydl = yt_dlp.YoutubeDL({})
        url_text = self.window.findChild(QLineEdit, "lineedit_url").text()
        list_info = []
        try:
            info_dict = ydl.extract_info(url=url_text, download=False)
            json_data = json.dumps(info_dict, indent=4)
            print(info_dict)
            document = json.loads(json_data)
            model = jsonmodel.JsonModel()
            model.load(document)
            self.window.findChild(QTreeView, "treeview_detailed").setModel(model)
            self.window.findChild(QTextEdit, "textbox_status").append(text_style("b", text_color("Green", "INFO: ")) + "Got Video Info!")

            title = info_dict.get("title", None)

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
                text_style("b", text_color("Red", "ERROR: ")) + "Unsupported URL: "+text_style("i", url_text))
            return False, list_info

        self.app.processEvents()
        return True, list_info

    def clear_temps(self):
        files = glob.glob(os.getcwd()+"/temp/downloaded.*")
        for file in files:
            os.remove(file)

    def escape_ansi(self, line):
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        return ansi_escape.sub('', line)

    def my_hook(self, d):
        if d['status'] == 'finished':
            print('\n\nDone downloading'+d["filename"]+'.\n')
            self.window.findChild(QTextEdit, "textbox_status").append(text_style(
                "b", text_color("Green", "DOWNLOAD: \t"))+"Done downloading "+text_color("Green", d["filename"])+".")

        if d['status'] == 'error':
            print('\n\nSomething went wrong with the download.\n')
            self.window.findChild(QTextEdit, "textbox_status").append(
                text_style("b", text_color("Green", "DOWNLOAD: \t"))+"Something went wrong with the download.")

        if d['status'] == 'downloading':
            self.window.findChild(QProgressBar, "progressbar_download").setValue(float(self.escape_ansi(d['_percent_str']).strip().replace("%", "")))

            status_line = text_style("b", text_color("Green", "DOWNLOAD: \t"))
            status_line += text_color("Blue", self.escape_ansi(d['_percent_str']))
            status_line += " of "
            status_line += text_style("i", text_color("Green", self.escape_ansi(d['filename'])))
            status_line += " ETA "
            status_line += text_color("Orange", self.escape_ansi(d['_eta_str']))
            self.window.findChild(QTextEdit, "textbox_status").append(status_line)

            self.app.processEvents()
            print(d['filename'], d['_percent_str'], d['_eta_str'])

    def click_download(self):
        infocheck = self.get_video_info()
        
        if not infocheck[0]:
            return
        
        safename = "".join([c for c in infocheck[1][0][1] if c.isalpha() or c.isdigit() or c == ' ']).rstrip()

        default_file_name = os.getcwd() + "/temp/" + safename

        self.save_video_location = QFileDialog.getSaveFileName(self, caption='Save File', dir=default_file_name, filter="ext (*)")
        print(self.save_video_location)

        if (self.save_video_location[0] == ""):
            return 
            #self.save_video_location = os.getcwd() + "/temp/download"
        else:
            self.save_video_location = self.save_video_location[0]

        try:
            os.makedirs(os.getcwd()+"/temp/")
        except:  # all good
            a = 0

        if (not os.path.isdir(os.getcwd()+"/temp/")):
            print("Can't find temp directory. Returning.")
            return False

        self.clear_temps()

        options = {
            'outtmpl': self.save_video_location+".%(ext)s",
            'fixup': "detect_or_warn",
            'noplaylist': True,
            'progress_hooks': [self.my_hook],
        }

        ydl = yt_dlp.YoutubeDL(options)
        ydl.add_post_processor(MyCustomPP(), when='post_process')
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
