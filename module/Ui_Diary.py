# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Diary.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import ConceptTable
from widget import FileTable
from DTPySide.DTWidget import DTPlainTextEdit
from widget import TextList

import DTPySide.DT_rc

class Ui_Diary(object):
    def setupUi(self, Diary):
        if not Diary.objectName():
            Diary.setObjectName(u"Diary")
        Diary.resize(943, 684)
        self.actionSwitch_Eidt_View = QAction(Diary)
        self.actionSwitch_Eidt_View.setObjectName(u"actionSwitch_Eidt_View")
        icon = QIcon()
        icon.addFile(u":/icon/white/white_slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSwitch_Eidt_View.setIcon(icon)
        self.actionPrevious_Day = QAction(Diary)
        self.actionPrevious_Day.setObjectName(u"actionPrevious_Day")
        icon1 = QIcon()
        icon1.addFile(u":/icon/white/white_chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrevious_Day.setIcon(icon1)
        self.actionNext_Day = QAction(Diary)
        self.actionNext_Day.setObjectName(u"actionNext_Day")
        icon2 = QIcon()
        icon2.addFile(u":/icon/white/white_chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNext_Day.setIcon(icon2)
        self.actionAdd_Line = QAction(Diary)
        self.actionAdd_Line.setObjectName(u"actionAdd_Line")
        icon3 = QIcon()
        icon3.addFile(u":/icon/white/white_plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Line.setIcon(icon3)
        self.actionDelete = QAction(Diary)
        self.actionDelete.setObjectName(u"actionDelete")
        icon4 = QIcon()
        icon4.addFile(u":/icon/white/white_trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon4)
        self.actionNext_Week = QAction(Diary)
        self.actionNext_Week.setObjectName(u"actionNext_Week")
        icon5 = QIcon()
        icon5.addFile(u":/icon/white/white_chevrons-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNext_Week.setIcon(icon5)
        self.actionPrevious_Week = QAction(Diary)
        self.actionPrevious_Week.setObjectName(u"actionPrevious_Week")
        icon6 = QIcon()
        icon6.addFile(u":/icon/white/white_chevrons-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrevious_Week.setIcon(icon6)
        self.actionNext_Line = QAction(Diary)
        self.actionNext_Line.setObjectName(u"actionNext_Line")
        self.actionNext_Line.setIcon(icon2)
        self.actionPrevious_Line = QAction(Diary)
        self.actionPrevious_Line.setObjectName(u"actionPrevious_Line")
        self.actionPrevious_Line.setIcon(icon1)
        self.actionFirst_Line = QAction(Diary)
        self.actionFirst_Line.setObjectName(u"actionFirst_Line")
        self.actionFirst_Line.setIcon(icon6)
        self.actionLast_Line = QAction(Diary)
        self.actionLast_Line.setObjectName(u"actionLast_Line")
        self.actionLast_Line.setIcon(icon5)
        self.actionFind_Text = QAction(Diary)
        self.actionFind_Text.setObjectName(u"actionFind_Text")
        icon7 = QIcon()
        icon7.addFile(u":/icon/white/white_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFind_Text.setIcon(icon7)
        self.horizontalLayout = QHBoxLayout(Diary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_whole = QSplitter(Diary)
        self.splitter_whole.setObjectName(u"splitter_whole")
        self.splitter_whole.setOrientation(Qt.Horizontal)
        self.stackedWidget = QStackedWidget(self.splitter_whole)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.verticalLayout = QVBoxLayout(self.page_edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textList = TextList(self.page_edit)
        self.textList.setObjectName(u"textList")
        self.textList.setMinimumSize(QSize(600, 400))

        self.verticalLayout.addWidget(self.textList)

        self.textEdit = DTPlainTextEdit(self.page_edit)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalLayout.setStretch(0, 15)
        self.verticalLayout.setStretch(1, 4)
        self.stackedWidget.addWidget(self.page_edit)
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.horizontalLayout_2 = QHBoxLayout(self.page_view)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textViewer = QTextBrowser(self.page_view)
        self.textViewer.setObjectName(u"textViewer")
        self.textViewer.setMinimumSize(QSize(600, 600))
        self.textViewer.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.textViewer)

        self.stackedWidget.addWidget(self.page_view)
        self.splitter_whole.addWidget(self.stackedWidget)
        self.splitter = QSplitter(self.splitter_whole)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.calendar = QCalendarWidget(self.splitter)
        self.calendar.setObjectName(u"calendar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendar.setMinimumSize(QSize(320, 270))
        self.calendar.setMaximumSize(QSize(16777215, 270))
        self.calendar.setFirstDayOfWeek(Qt.Monday)
        self.calendar.setGridVisible(True)
        self.calendar.setNavigationBarVisible(False)
        self.splitter.addWidget(self.calendar)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_concept = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_concept.setSpacing(0)
        self.verticalLayout_concept.setObjectName(u"verticalLayout_concept")
        self.verticalLayout_concept.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_concept.addWidget(self.label)

        self.conceptTable = ConceptTable(self.layoutWidget)
        self.conceptTable.setObjectName(u"conceptTable")

        self.verticalLayout_concept.addWidget(self.conceptTable)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_file = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_file.setSpacing(0)
        self.verticalLayout_file.setObjectName(u"verticalLayout_file")
        self.verticalLayout_file.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_file.addWidget(self.label_2)

        self.fileTable = FileTable(self.layoutWidget1)
        self.fileTable.setObjectName(u"fileTable")

        self.verticalLayout_file.addWidget(self.fileTable)

        self.splitter.addWidget(self.layoutWidget1)
        self.splitter_whole.addWidget(self.splitter)

        self.horizontalLayout.addWidget(self.splitter_whole)


        self.retranslateUi(Diary)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Diary)
    # setupUi

    def retranslateUi(self, Diary):
        Diary.setWindowTitle(QCoreApplication.translate("Diary", u"Diary", None))
        self.actionSwitch_Eidt_View.setText(QCoreApplication.translate("Diary", u"Switch Eidt / View", None))
#if QT_CONFIG(tooltip)
        self.actionSwitch_Eidt_View.setToolTip(QCoreApplication.translate("Diary", u"Switch Eidt / View", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSwitch_Eidt_View.setShortcut(QCoreApplication.translate("Diary", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Day.setText(QCoreApplication.translate("Diary", u"Previous Day", None))
#if QT_CONFIG(tooltip)
        self.actionPrevious_Day.setToolTip(QCoreApplication.translate("Diary", u"Previous Day", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPrevious_Day.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Day.setText(QCoreApplication.translate("Diary", u"Next Day", None))
#if QT_CONFIG(tooltip)
        self.actionNext_Day.setToolTip(QCoreApplication.translate("Diary", u"Next Day", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNext_Day.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Line.setText(QCoreApplication.translate("Diary", u"Add Line", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_Line.setToolTip(QCoreApplication.translate("Diary", u"Add Line", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAdd_Line.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("Diary", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("Diary", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Week.setText(QCoreApplication.translate("Diary", u"Next Week", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Week.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Week.setText(QCoreApplication.translate("Diary", u"Previous Week", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Week.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+Alt+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Line.setText(QCoreApplication.translate("Diary", u"Next Line", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Line.setText(QCoreApplication.translate("Diary", u"Previous Line", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionFirst_Line.setText(QCoreApplication.translate("Diary", u"First Line", None))
#if QT_CONFIG(shortcut)
        self.actionFirst_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionLast_Line.setText(QCoreApplication.translate("Diary", u"Last Line", None))
#if QT_CONFIG(shortcut)
        self.actionLast_Line.setShortcut(QCoreApplication.translate("Diary", u"Alt+Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionFind_Text.setText(QCoreApplication.translate("Diary", u"Find Text", None))
#if QT_CONFIG(shortcut)
        self.actionFind_Text.setShortcut(QCoreApplication.translate("Diary", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("Diary", u"Concept", None))
        self.label_2.setText(QCoreApplication.translate("Diary", u"File", None))
    # retranslateUi

