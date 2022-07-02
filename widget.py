# This Python file uses the following encoding: utf-8
import json
import os
import sys
from pathlib import Path

import yt_dlp
from PySide6.QtCore import QFile
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


class Widget(QWidget):

    def widget_by_name(self, name):
        return self.findChildren(QWidget, name)[0]

    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        self.setWindowTitle("ClipEZ-Next")

        self.widget_by_name("button_cleartext").clicked.connect(self.clear_url)
        self.widget_by_name("button_getinfo").clicked.connect(self.get_video_info)
        self.widget_by_name("button_downloadstart").clicked.connect(self.click_download)
        self.widget_by_name("lineedit_url").returnPressed.connect(self.click_download)
        self.widget_by_name("lineedit_url").textChanged.connect(self.enable_clear_text_button)


        self.widget_by_name("image_thumb").setMinimumWidth(self.widget_by_name("treeview_detailed").height()*9/16)
        self.widget_by_name("image_thumb").setMaximumWidth(self.widget_by_name("treeview_detailed").height()*9/16)
        self.widget_by_name("image_thumb").setFixedWidth(self.widget_by_name("treeview_detailed").height()*9/16)

        self.enable_clear_text_button()

    def get_video_info(self):
        self.widget_by_name("textbox_status").append(styletext("b", colortext("Green", "INFO: "))+"Getting Video Info...")
        ydl = yt_dlp.YoutubeDL({})
        url_text = self.widget_by_name("lineedit_url").text()
        try:
            info_dict = ydl.extract_info(url=url_text, download=False)
            json_data = json.dumps(info_dict, indent=4)
            print(info_dict)
            document = json.loads(json_data)
            model = jsonmodel.JsonModel()
            model.load(document)
            self.widget_by_name("treeview_detailed").setModel(model)
            self.widget_by_name("textbox_status").append(styletext("b", colortext("Green", "INFO: ")) + "Got Video Info!")

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
                self.widget_by_name("table_simple").insertRow(self.widget_by_name("table_simple").rowCount())
                self.widget_by_name("table_simple").setItem(i, 0, QTableWidgetItem(list_info[i][0]))
                self.widget_by_name("table_simple").setItem(i, 1, QTableWidgetItem(list_info[i][1]))

            thumb_url = info_dict.get("thumbnail", None)
            if thumb_url != None:
                with urllib.request.urlopen(thumb_url) as _url:
                    data = _url.read()
                    px = QPixmap()
                    px.loadFromData(data)
                    self.widget_by_name("image_thumb").setPixmap(px)

        except Exception as e:
            print(e)
            self.widget_by_name("textbox_status").append(styletext("b", colortext("Red", "ERROR: ")) + "Unsupported URL: "+styletext("i", url_text))

    def click_download(self):
        self.get_video_info()

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

        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    widget = Widget()
    widget.show()
    sys.exit(app.exec())
