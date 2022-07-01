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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(896, 555)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        self.button_downloadstart = QPushButton(self.tab)
        self.button_downloadstart.setObjectName(u"button_downloadstart")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.button_downloadstart)

        self.textbox_status = QTextEdit(self.tab)
        self.textbox_status.setObjectName(u"textbox_status")
        self.textbox_status.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_status.sizePolicy().hasHeightForWidth())
        self.textbox_status.setSizePolicy(sizePolicy)
        self.textbox_status.setMaximumSize(QSize(16777215, 16777215))
        self.textbox_status.setLineWrapMode(QTextEdit.NoWrap)
        self.textbox_status.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.textbox_status)

        self.lineedit_url = QLineEdit(self.tab)
        self.lineedit_url.setObjectName(u"lineedit_url")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.lineedit_url)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.button_downloadstart.setText(QCoreApplication.translate("Widget", u"Go", None))
        self.label.setText(QCoreApplication.translate("Widget", u"VIdeo URL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Download Video", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Sync Channels", None))
    # retranslateUi

