# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QTreeView, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1273, 828)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(Widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabs_overall = QTabWidget(Widget)
        self.tabs_overall.setObjectName(u"tabs_overall")
        self.tab_downloadvideo = QWidget()
        self.tab_downloadvideo.setObjectName(u"tab_downloadvideo")
        self.verticalLayout_3 = QVBoxLayout(self.tab_downloadvideo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupbox_videourl = QGroupBox(self.tab_downloadvideo)
        self.groupbox_videourl.setObjectName(u"groupbox_videourl")
        self.verticalLayout = QVBoxLayout(self.groupbox_videourl)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineedit_url = QLineEdit(self.groupbox_videourl)
        self.lineedit_url.setObjectName(u"lineedit_url")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineedit_url.sizePolicy().hasHeightForWidth())
        self.lineedit_url.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lineedit_url)

        self.button_cleartext = QPushButton(self.groupbox_videourl)
        self.button_cleartext.setObjectName(u"button_cleartext")
        self.button_cleartext.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_cleartext.sizePolicy().hasHeightForWidth())
        self.button_cleartext.setSizePolicy(sizePolicy2)
        self.button_cleartext.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.button_cleartext)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_getinfo = QPushButton(self.groupbox_videourl)
        self.button_getinfo.setObjectName(u"button_getinfo")
        sizePolicy2.setHeightForWidth(self.button_getinfo.sizePolicy().hasHeightForWidth())
        self.button_getinfo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.button_getinfo)

        self.button_downloadstart = QPushButton(self.groupbox_videourl)
        self.button_downloadstart.setObjectName(u"button_downloadstart")
        sizePolicy2.setHeightForWidth(self.button_downloadstart.sizePolicy().hasHeightForWidth())
        self.button_downloadstart.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.button_downloadstart)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupbox_videourl)

        self.groupbox_videoinfo = QGroupBox(self.tab_downloadvideo)
        self.groupbox_videoinfo.setObjectName(u"groupbox_videoinfo")
        self.gridLayout_3 = QGridLayout(self.groupbox_videoinfo)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabs_videoinfo = QTabWidget(self.groupbox_videoinfo)
        self.tabs_videoinfo.setObjectName(u"tabs_videoinfo")
        self.tab_videoinfo_simple = QWidget()
        self.tab_videoinfo_simple.setObjectName(u"tab_videoinfo_simple")
        self.gridLayout_4 = QGridLayout(self.tab_videoinfo_simple)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget = QTableWidget(self.tab_videoinfo_simple)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabs_videoinfo.addTab(self.tab_videoinfo_simple, "")
        self.tab_videoinfo_detailed = QWidget()
        self.tab_videoinfo_detailed.setObjectName(u"tab_videoinfo_detailed")
        self.gridLayout_2 = QGridLayout(self.tab_videoinfo_detailed)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeview_detailed = QTreeView(self.tab_videoinfo_detailed)
        self.treeview_detailed.setObjectName(u"treeview_detailed")

        self.gridLayout_2.addWidget(self.treeview_detailed, 0, 0, 1, 1)

        self.tabs_videoinfo.addTab(self.tab_videoinfo_detailed, "")

        self.gridLayout_3.addWidget(self.tabs_videoinfo, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupbox_videoinfo)

        self.groupbox_status = QGroupBox(self.tab_downloadvideo)
        self.groupbox_status.setObjectName(u"groupbox_status")
        self.verticalLayout_2 = QVBoxLayout(self.groupbox_status)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textbox_status = QTextEdit(self.groupbox_status)
        self.textbox_status.setObjectName(u"textbox_status")
        self.textbox_status.setEnabled(True)
        sizePolicy.setHeightForWidth(self.textbox_status.sizePolicy().hasHeightForWidth())
        self.textbox_status.setSizePolicy(sizePolicy)
        self.textbox_status.setMaximumSize(QSize(16777215, 16777215))
        self.textbox_status.setFrameShadow(QFrame.Sunken)
        self.textbox_status.setLineWrapMode(QTextEdit.NoWrap)
        self.textbox_status.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textbox_status)

        self.progressbar_download = QProgressBar(self.groupbox_status)
        self.progressbar_download.setObjectName(u"progressbar_download")
        self.progressbar_download.setValue(0)
        self.progressbar_download.setInvertedAppearance(False)

        self.verticalLayout_2.addWidget(self.progressbar_download)


        self.verticalLayout_3.addWidget(self.groupbox_status)

        self.tabs_overall.addTab(self.tab_downloadvideo, "")
        self.tab_syncpanel = QWidget()
        self.tab_syncpanel.setObjectName(u"tab_syncpanel")
        self.gridLayout_5 = QGridLayout(self.tab_syncpanel)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.dial = QDial(self.tab_syncpanel)
        self.dial.setObjectName(u"dial")

        self.gridLayout_5.addWidget(self.dial, 0, 0, 1, 1)

        self.tabs_overall.addTab(self.tab_syncpanel, "")

        self.verticalLayout_4.addWidget(self.tabs_overall)


        self.retranslateUi(Widget)

        self.tabs_overall.setCurrentIndex(0)
        self.tabs_videoinfo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"ClipEz-Next", None))
        self.groupbox_videourl.setTitle(QCoreApplication.translate("Widget", u"Video URL", None))
        self.button_cleartext.setText(QCoreApplication.translate("Widget", u"Clear Text", None))
        self.button_getinfo.setText(QCoreApplication.translate("Widget", u"Get Info", None))
        self.button_downloadstart.setText(QCoreApplication.translate("Widget", u"Download", None))
        self.groupbox_videoinfo.setTitle(QCoreApplication.translate("Widget", u"Video Info", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"key", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"value", None));
        self.tabs_videoinfo.setTabText(self.tabs_videoinfo.indexOf(self.tab_videoinfo_simple), QCoreApplication.translate("Widget", u"Simple", None))
        self.tabs_videoinfo.setTabText(self.tabs_videoinfo.indexOf(self.tab_videoinfo_detailed), QCoreApplication.translate("Widget", u"Detailed", None))
        self.groupbox_status.setTitle(QCoreApplication.translate("Widget", u"Status", None))
        self.tabs_overall.setTabText(self.tabs_overall.indexOf(self.tab_downloadvideo), QCoreApplication.translate("Widget", u"Download Video", None))
        self.tabs_overall.setTabText(self.tabs_overall.indexOf(self.tab_syncpanel), QCoreApplication.translate("Widget", u"Sync Channels", None))
    # retranslateUi

