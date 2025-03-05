# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 671)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_3 = QVBoxLayout(self.page1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.page1)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)

        self.stackedWidget.addWidget(self.page1)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_6 = QVBoxLayout(self.page3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit_3 = QTextEdit(self.page3)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.verticalLayout_6.addWidget(self.textEdit_3)

        self.frame_6 = QFrame(self.page3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(378, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.choose_file = QPushButton(self.frame_6)
        self.choose_file.setObjectName(u"choose_file")

        self.horizontalLayout_4.addWidget(self.choose_file)

        self.horizontalSpacer_4 = QSpacerItem(378, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page3)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.horizontalLayout_3 = QHBoxLayout(self.page2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.page2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(182, 16777215))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 118, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.name_line = QLineEdit(self.frame_4)
        self.name_line.setObjectName(u"name_line")

        self.verticalLayout_4.addWidget(self.name_line)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.user_line = QLineEdit(self.frame_4)
        self.user_line.setObjectName(u"user_line")

        self.verticalLayout_4.addWidget(self.user_line)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.pass_line = QLineEdit(self.frame_4)
        self.pass_line.setObjectName(u"pass_line")

        self.verticalLayout_4.addWidget(self.pass_line)

        self.check_db_btn = QPushButton(self.frame_4)
        self.check_db_btn.setObjectName(u"check_db_btn")

        self.verticalLayout_4.addWidget(self.check_db_btn)

        self.check_db_oper_btn = QPushButton(self.frame_4)
        self.check_db_oper_btn.setObjectName(u"check_db_oper_btn")

        self.verticalLayout_4.addWidget(self.check_db_oper_btn)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 117, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.textEdit_2 = QTextEdit(self.page2)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout_3.addWidget(self.textEdit_2)

        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 81))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.net_btn = QPushButton(self.frame)
        self.net_btn.setObjectName(u"net_btn")

        self.horizontalLayout.addWidget(self.net_btn)

        self.disk_btn = QPushButton(self.frame)
        self.disk_btn.setObjectName(u"disk_btn")

        self.horizontalLayout.addWidget(self.disk_btn)

        self.file_btn = QPushButton(self.frame)
        self.file_btn.setObjectName(u"file_btn")

        self.horizontalLayout.addWidget(self.file_btn)

        self.cpu_btn = QPushButton(self.frame)
        self.cpu_btn.setObjectName(u"cpu_btn")

        self.horizontalLayout.addWidget(self.cpu_btn)

        self.serv_btn = QPushButton(self.frame)
        self.serv_btn.setObjectName(u"serv_btn")

        self.horizontalLayout.addWidget(self.serv_btn)

        self.db_btn = QPushButton(self.frame)
        self.db_btn.setObjectName(u"db_btn")

        self.horizontalLayout.addWidget(self.db_btn)


        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choose_file.setText(QCoreApplication.translate("MainWindow", u"\u0412\u042b\u0411\u0420\u0410\u0422\u042c \n"
" \u0424\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0431\u0430\u0437\u044b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.check_db_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c\n"
" \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.check_db_oper_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c\n"
" \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.net_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430\n"
" \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0430", None))
        self.disk_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430\n"
"\u0414\u0438\u0441\u043a\u0430 ", None))
        self.file_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430\n"
"\u0444\u0430\u0439\u043b\u0430 ", None))
        self.cpu_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430\n"
" CPU/RAM", None))
        self.serv_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430\n"
" \u0441\u0435\u0440\u0432\u0438\u0441\u043e\u0432", None))
        self.db_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430\n"
" \u0411\u0414", None))
    # retranslateUi

