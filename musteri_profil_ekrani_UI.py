# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musteri_profil_ekrani_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowMusProfil(object):
    def setupUi(self, MainWindowMusProfil):
        MainWindowMusProfil.setObjectName("MainWindowMusProfil")
        MainWindowMusProfil.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindowMusProfil)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.adSoyadLabel = QtWidgets.QLabel(self.centralwidget)
        self.adSoyadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.adSoyadLabel.setObjectName("adSoyadLabel")
        self.gridLayout.addWidget(self.adSoyadLabel, 6, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 2)
        self.telNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.telNoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.telNoLabel.setObjectName("telNoLabel")
        self.gridLayout.addWidget(self.telNoLabel, 8, 2, 1, 2)
        self.kimlikNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.kimlikNoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kimlikNoLabel.setObjectName("kimlikNoLabel")
        self.gridLayout.addWidget(self.kimlikNoLabel, 7, 2, 1, 2)
        self.mailLabel = QtWidgets.QLabel(self.centralwidget)
        self.mailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mailLabel.setObjectName("mailLabel")
        self.gridLayout.addWidget(self.mailLabel, 9, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 2)
        self.anaSayfaButton = QtWidgets.QPushButton(self.centralwidget)
        self.anaSayfaButton.setObjectName("anaSayfaButton")
        self.gridLayout.addWidget(self.anaSayfaButton, 1, 0, 1, 2)
        self.yenileButton = QtWidgets.QPushButton(self.centralwidget)
        self.yenileButton.setObjectName("yenileButton")
        self.gridLayout.addWidget(self.yenileButton, 1, 2, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindowMusProfil.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowMusProfil)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindowMusProfil.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowMusProfil)
        self.statusbar.setObjectName("statusbar")
        MainWindowMusProfil.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowMusProfil)
        QtCore.QMetaObject.connectSlotsByName(MainWindowMusProfil)

    def retranslateUi(self, MainWindowMusProfil):
        _translate = QtCore.QCoreApplication.translate
        MainWindowMusProfil.setWindowTitle(_translate("MainWindowMusProfil", "Müşteri Profil Ekranı"))
        self.adSoyadLabel.setText(_translate("MainWindowMusProfil", "NONE"))
        self.label_5.setText(_translate("MainWindowMusProfil", "Mail "))
        self.telNoLabel.setText(_translate("MainWindowMusProfil", "NONE"))
        self.kimlikNoLabel.setText(_translate("MainWindowMusProfil", "NONE"))
        self.mailLabel.setText(_translate("MainWindowMusProfil", "NONE"))
        self.label.setText(_translate("MainWindowMusProfil", "Ad Soyad"))
        self.label_3.setText(_translate("MainWindowMusProfil", "Tc Kimlik No"))
        self.label_4.setText(_translate("MainWindowMusProfil", "Telefon No"))
        self.anaSayfaButton.setText(_translate("MainWindowMusProfil", "Ana Sayfa"))
        self.yenileButton.setText(_translate("MainWindowMusProfil", "Yenile"))
