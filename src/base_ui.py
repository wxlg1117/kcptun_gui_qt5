#!/usr/bin/env python3
# -*- coding:utf-8 -*-
U"""
basic grid
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class BasicWindow(QMainWindow):

    def __init__(self):
        u"""
        init
        """
        super().__init__()
        self.elements = self.setupUi()

        self.parameters = {
            "-l": self.l_line,
            "-r": self.r_line,
            "--key": self.key_line,
            "--crypt": self.crypt_box,
            "--mode": self.mode_box,
            "--conn": self.conn_line,
            "--autoexpire": self.autoexpire_line,
            "--mtu": self.mtu_line,
            "--sndwnd": self.sndwnd_line,
            "--rcvwnd": self.rcvwnd_line,
            "--datashard": self.datashard_line,
            "--parityshard": self.parityshard_line,
            "--dscp": self.dscp_line,
            "--nocomp": True,
            "-p": self.p_line,
            "--scavengettl": self.scaven_line
        }

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(1100, 610)
        self.process = QProcess()
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QRect(20, 230, 632, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scaven_line = QLineEdit(self.gridLayoutWidget)
        self.scaven_line.setEnabled(False)
        self.scaven_line.setObjectName("scaven_line")
        self.gridLayout_2.addWidget(self.scaven_line, 6, 1, 1, 1)
        self.rcvwnd = QCheckBox(self.gridLayoutWidget)
        self.rcvwnd.setEnabled(False)
        self.rcvwnd.setObjectName("rcvwnd")
        self.gridLayout_2.addWidget(self.rcvwnd, 4, 2, 1, 1)
        self.dscp_line = QLineEdit(self.gridLayoutWidget)
        self.dscp_line.setEnabled(False)
        self.dscp_line.setObjectName("dscp_line")
        self.gridLayout_2.addWidget(self.dscp_line, 5, 1, 1, 1)
        self.mtu = QCheckBox(self.gridLayoutWidget)
        self.mtu.setEnabled(False)
        self.mtu.setObjectName("mtu")
        self.gridLayout_2.addWidget(self.mtu, 3, 2, 1, 1)
        self.nocomp = QCheckBox(self.gridLayoutWidget)
        self.nocomp.setEnabled(False)
        self.nocomp.setObjectName("nocomp")
        self.gridLayout_2.addWidget(self.nocomp, 1, 2, 1, 1)
        self.key_line = QLineEdit(self.gridLayoutWidget)
        self.key_line.setEnabled(False)
        self.key_line.setObjectName("key_line")
        self.gridLayout_2.addWidget(self.key_line, 0, 1, 1, 3)
        self.nocomp_line = QLineEdit(self.gridLayoutWidget)
        self.nocomp_line.setEnabled(False)
        self.nocomp_line.setObjectName("nocomp_line")
        self.gridLayout_2.addWidget(self.nocomp_line, 1, 3, 1, 1)
        self.mtu_line = QLineEdit(self.gridLayoutWidget)
        self.mtu_line.setEnabled(False)
        self.mtu_line.setObjectName("mtu_line")
        self.gridLayout_2.addWidget(self.mtu_line, 3, 3, 1, 1)
        self.conn = QCheckBox(self.gridLayoutWidget)
        self.conn.setEnabled(False)
        self.conn.setObjectName("conn")
        self.gridLayout_2.addWidget(self.conn, 3, 0, 1, 1)
        self.crypt = QCheckBox(self.gridLayoutWidget)
        self.crypt.setEnabled(False)
        self.crypt.setObjectName("crypt")
        self.gridLayout_2.addWidget(self.crypt, 1, 0, 1, 1)
        self.parityshard = QCheckBox(self.gridLayoutWidget)
        self.parityshard.setEnabled(False)
        self.parityshard.setObjectName("parityshard")
        self.gridLayout_2.addWidget(self.parityshard, 2, 2, 1, 1)
        self.datashard_line = QLineEdit(self.gridLayoutWidget)
        self.datashard_line.setEnabled(False)
        self.datashard_line.setObjectName("datashard_line")
        self.gridLayout_2.addWidget(self.datashard_line, 2, 1, 1, 1)
        self.sndwnd = QCheckBox(self.gridLayoutWidget)
        self.sndwnd.setEnabled(False)
        self.sndwnd.setObjectName("sndwnd")
        self.gridLayout_2.addWidget(self.sndwnd, 4, 0, 1, 1)
        self.sndwnd_line = QLineEdit(self.gridLayoutWidget)
        self.sndwnd_line.setEnabled(False)
        self.sndwnd_line.setObjectName("sndwnd_line")
        self.gridLayout_2.addWidget(self.sndwnd_line, 4, 1, 1, 1)
        self.parityshard_line = QLineEdit(self.gridLayoutWidget)
        self.parityshard_line.setEnabled(False)
        self.parityshard_line.setObjectName("parityshard_line")
        self.gridLayout_2.addWidget(self.parityshard_line, 2, 3, 1, 1)
        self.key = QCheckBox(self.gridLayoutWidget)
        self.key.setEnabled(False)
        self.key.setObjectName("key")
        self.gridLayout_2.addWidget(self.key, 0, 0, 1, 1)
        self.datashard = QCheckBox(self.gridLayoutWidget)
        self.datashard.setEnabled(False)
        self.datashard.setObjectName("datashard")
        self.gridLayout_2.addWidget(self.datashard, 2, 0, 1, 1)
        self.autoexpire = QCheckBox(self.gridLayoutWidget)
        self.autoexpire.setEnabled(False)
        self.autoexpire.setObjectName("autoexpire")
        self.gridLayout_2.addWidget(self.autoexpire, 5, 2, 1, 1)
        self.dscp = QCheckBox(self.gridLayoutWidget)
        self.dscp.setEnabled(False)
        self.dscp.setObjectName("dscp")
        self.gridLayout_2.addWidget(self.dscp, 5, 0, 1, 1)
        self.conn_line = QLineEdit(self.gridLayoutWidget)
        self.conn_line.setEnabled(False)
        self.conn_line.setObjectName("conn_line")
        self.gridLayout_2.addWidget(self.conn_line, 3, 1, 1, 1)
        self.crypt_box = QComboBox(self.gridLayoutWidget)
        self.crypt_box.setEnabled(False)
        self.crypt_box.setObjectName("comboBox")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.crypt_box.addItem("")
        self.gridLayout_2.addWidget(self.crypt_box, 1, 1, 1, 1)
        self.rcvwnd_line = QLineEdit(self.gridLayoutWidget)
        self.rcvwnd_line.setEnabled(False)
        self.rcvwnd_line.setObjectName("rcvwnd_line")
        self.gridLayout_2.addWidget(self.rcvwnd_line, 4, 3, 1, 1)
        self.autoexpire_line = QLineEdit(self.gridLayoutWidget)
        self.autoexpire_line.setEnabled(False)
        self.autoexpire_line.setObjectName("autoexpire_line")
        self.gridLayout_2.addWidget(self.autoexpire_line, 5, 3, 1, 1)
        self.scave = QCheckBox(self.gridLayoutWidget)
        self.scave.setEnabled(False)
        self.scave.setObjectName("scave")
        self.gridLayout_2.addWidget(self.scave, 6, 0, 1, 1)
        self.gridLayoutWidget_2 = QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QRect(20, 100, 631, 103))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.r_line = QLineEdit(self.gridLayoutWidget_2)
        self.r_line.setEnabled(False)
        self.r_line.setObjectName("r_line")
        self.gridLayout_3.addWidget(self.r_line, 1, 1, 1, 1)
        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 2, 1, 1)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.p_line = QLineEdit(self.gridLayoutWidget_2)
        self.p_line.setEnabled(False)
        self.p_line.setObjectName("p_line")
        self.gridLayout_3.addWidget(self.p_line, 1, 3, 1, 1)
        self.l_line = QLineEdit(self.gridLayoutWidget_2)
        self.l_line.setEnabled(False)
        self.l_line.setObjectName("l_line")
        self.gridLayout_3.addWidget(self.l_line, 0, 1, 1, 1)
        self.label_6 = QLabel(self.centralWidget)
        self.label_6.setGeometry(QRect(20, 80, 114, 18))
        self.label_6.setObjectName("label_6")
        self.label_5 = QLabel(self.centralWidget)
        self.label_5.setGeometry(QRect(20, 180, 337, 77))
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget_3 = QWidget(self.centralWidget)
        self.gridLayoutWidget_3.setGeometry(QRect(660, 100, 431, 101))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.interval_line = QLineEdit(self.gridLayoutWidget_3)
        self.interval_line.setEnabled(False)
        self.interval_line.setObjectName("interval_line")
        self.gridLayout_4.addWidget(self.interval_line, 1, 1, 1, 1)
        self.mode = QCheckBox(self.gridLayoutWidget_3)
        self.mode.setEnabled(False)
        self.mode.setObjectName("mode")
        self.gridLayout_4.addWidget(self.mode, 0, 0, 1, 1)
        self.mode_box = QComboBox(self.gridLayoutWidget_3)
        self.mode_box.setEnabled(False)
        self.mode_box.setObjectName("mode_box")
        self.mode_box.addItem("")
        self.mode_box.addItem("")
        self.mode_box.addItem("")
        self.mode_box.addItem("")
        self.mode_box.addItem("")
        self.gridLayout_4.addWidget(self.mode_box, 0, 1, 1, 1)
        self.interval = QCheckBox(self.gridLayoutWidget_3)
        self.interval.setEnabled(False)
        self.interval.setObjectName("interval")
        self.gridLayout_4.addWidget(self.interval, 1, 0, 1, 1)
        self.nodelay = QCheckBox(self.gridLayoutWidget_3)
        self.nodelay.setEnabled(False)
        self.nodelay.setObjectName("nodelay")
        self.gridLayout_4.addWidget(self.nodelay, 0, 2, 1, 1)
        self.resend = QCheckBox(self.gridLayoutWidget_3)
        self.resend.setEnabled(False)
        self.resend.setObjectName("resend")
        self.gridLayout_4.addWidget(self.resend, 1, 2, 1, 1)
        self.gridLayoutWidget_4 = QWidget(self.centralWidget)
        self.gridLayoutWidget_4.setGeometry(QRect(660, 230, 431, 281))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.command = QTextEdit(self.gridLayoutWidget_4)
        self.command.setReadOnly(True)
        self.gridLayout_5.addWidget(self.command)
        self.output = QTextEdit(self.gridLayoutWidget_4)
        self.command.setReadOnly(True)
        self.output.setObjectName("scrollArea")
        self.gridLayout_5.addWidget(self.output, 3, 0, 1, 2)
        self.horizontalLayoutWidget = QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QRect(660, 520, 431, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start = QPushButton(self.horizontalLayoutWidget)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.stop = QPushButton(self.horizontalLayoutWidget)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.hide_button = QPushButton(self.horizontalLayoutWidget)
        self.hide_button.setObjectName("hide")
        self.horizontalLayout.addWidget(self.hide_button)
        self.quit = QPushButton(self.horizontalLayoutWidget)
        self.quit.setObjectName("quit")
        self.horizontalLayout.addWidget(self.quit)
        self.gridLayoutWidget_5 = QWidget(self.centralWidget)
        self.gridLayoutWidget_5.setGeometry(QRect(20, 0, 1071, 80))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.exe_select = QPushButton(self.gridLayoutWidget_5)
        self.exe_select.setObjectName("exe_select")
        self.gridLayout_6.addWidget(self.exe_select, 0, 3, 1, 1)
        self.json_path = QLineEdit(self.gridLayoutWidget_5)
        self.json_path.setEnabled(True)
        self.json_path.setObjectName("json_path")
        self.gridLayout_6.addWidget(self.json_path, 1, 2, 1, 1)
        self.json_select = QPushButton(self.gridLayoutWidget_5)
        self.json_select.setObjectName("json_select")
        self.gridLayout_6.addWidget(self.json_select, 1, 3, 1, 1)
        self.json = QCheckBox(self.gridLayoutWidget_5)
        self.json.setObjectName("json")
        self.json.setChecked(True)
        self.gridLayout_6.addWidget(self.json, 1, 1, 1, 1)
        self.label_4 = QLabel(self.gridLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 1, 1, 1)
        self.executable = QLineEdit(self.gridLayoutWidget_5)
        self.executable.setObjectName("executable")
        self.gridLayout_6.addWidget(self.executable, 0, 2, 1, 1)
        self.create = QComboBox(self.gridLayoutWidget_5)
        self.create.setObjectName("create")
        self.create.addItem("")
        self.gridLayout_6.addWidget(self.create, 0, 0, 1, 1)
        self.label_7 = QLabel(self.centralWidget)
        self.label_7.setGeometry(QRect(660, 210, 57, 18))
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self.centralWidget)
        self.label_8.setGeometry(QRect(660, 80, 57, 18))
        self.label_8.setObjectName("label_8")
        self.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar()
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)

        self.retranslateUi()
        self.hide_button.clicked.connect(self.hide)
        self.quit.clicked.connect(self.close)
        QMetaObject.connectSlotsByName(self)

        return {
            self.key: self.key_line,
            self.nocomp: self.nocomp_line,
            self.datashard: self.datashard_line,
            self.conn: self.conn_line,
            self.sndwnd: self.sndwnd_line,
            self.dscp: self.dscp_line,
            self.scave: self.scaven_line,
            self.parityshard: self.parityshard_line,
            self.mtu: self.mtu_line,
            self.rcvwnd: self.rcvwnd_line,
            self.autoexpire: self.autoexpire_line,
            self.interval: self.interval_line,
            # self.keepalive: self.keepalive_line,
            # self.sockbuf: self.sockbuf_line,
            self.crypt: self.crypt_box,
            self.mode: self.mode_box
        }

    def retranslateUi(self,):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rcvwnd.setText(_translate("MainWindow", "接收窗口（rcvwnd）"))
        self.mtu.setText(_translate("MainWindow", "MTU大小（mtu）"))
        self.nocomp.setText(_translate("MainWindow", "禁用压缩（nocomp）"))
        self.conn.setText(_translate("MainWindow", "连接数（conn）"))
        self.crypt.setText(_translate("MainWindow", "加密方式*（crypt）"))
        self.parityshard.setText(_translate("MainWindow", "校验块*（parityshard）"))
        self.sndwnd.setText(_translate("MainWindow", "发送窗口（sndwnd）"))
        self.key.setText(_translate("MainWindow", "通讯秘钥*（key）"))
        self.datashard.setText(_translate("MainWindow", "数据块*（datashard）"))
        self.autoexpire.setText(_translate("MainWindow", "过期时间（autoexpire）"))
        self.dscp.setText(_translate("MainWindow", "数据包优先级（dscp）"))
        self.crypt_box.setItemText(0, _translate("MainWindow", "aes"))
        self.crypt_box.setItemText(1, _translate("MainWindow", "aes-128"))
        self.crypt_box.setItemText(2, _translate("MainWindow", "aes-192"))
        self.crypt_box.setItemText(3, _translate("MainWindow", "salsa20"))
        self.crypt_box.setItemText(4, _translate("MainWindow", "blowfish"))
        self.crypt_box.setItemText(5, _translate("MainWindow", "twofish"))
        self.crypt_box.setItemText(6, _translate("MainWindow", "cast5"))
        self.crypt_box.setItemText(7, _translate("MainWindow", "3des"))
        self.crypt_box.setItemText(8, _translate("MainWindow", "tea"))
        self.crypt_box.setItemText(9, _translate("MainWindow", "xtea"))
        self.crypt_box.setItemText(10, _translate("MainWindow", "xor"))
        self.crypt_box.setItemText(11, _translate("MainWindow", "sm4"))
        self.crypt_box.setItemText(12, _translate("MainWindow", "none"))
        self.scave.setText(_translate("MainWindow", "失效会话保留时间（scavengettl）"))
        self.label.setText(_translate("MainWindow", "KCP服务器地址（r）"))
        self.label_3.setText(_translate("MainWindow", "端口"))
        self.label.setText(_translate("MainWindow", "本地侦听端口（l）"))
        self.label_2.setText(_translate("MainWindow", "KCP服务器地址（r）"))
        self.label_6.setText(_translate("MainWindow", "基本参数"))
        self.label_5.setText(_translate("MainWindow", "可选参数（*需要与服务器端一致）"))
        self.mode.setText(_translate("MainWindow", "模式选择（mode）"))
        self.mode_box.setItemText(0, _translate("MainWindow", "fast3"))
        self.mode_box.setItemText(1, _translate("MainWindow", "fast2"))
        self.mode_box.setItemText(2, _translate("MainWindow", "fast"))
        self.mode_box.setItemText(3, _translate("MainWindow", "normal"))
        self.mode_box.setItemText(4, _translate("MainWindow", "manul"))
        self.interval.setText(_translate("MainWindow", "间隔时间（interval）"))
        self.nodelay.setText(_translate("MainWindow", "启用（nodelay）"))
        self.resend.setText(_translate("MainWindow", "快速重传（resend）"))
        self.start.setText(_translate("MainWindow", "运行"))
        self.stop.setText(_translate("MainWindow", "停止"))
        self.hide_button.setText(_translate("MainWindow", "隐藏"))
        self.quit.setText(_translate("MainWindow", "退出"))
        self.exe_select.setText(_translate("MainWindow", "浏览"))
        self.json_select.setText(_translate("MainWindow", "浏览"))
        self.json.setText(_translate("MainWindow", "使用配置文件（json）"))
        self.label_4.setText(_translate("MainWindow", "KCPTun客户端路径"))
        self.create.setItemText(0, _translate("MainWindow", "create new"))
        self.label_7.setText(_translate("MainWindow", "命令"))
        self.label_8.setText(_translate("MainWindow", "传输模式"))