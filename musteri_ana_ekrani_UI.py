# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musteri_ana_ekrani_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowMusAnaEkran(object):
    def setupUi(self, MainWindowMusAnaEkran):
        MainWindowMusAnaEkran.setObjectName("MainWindowMusAnaEkran")
        MainWindowMusAnaEkran.resize(800, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindowMusAnaEkran)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxKoltuk = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxKoltuk.setObjectName("comboBoxKoltuk")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.comboBoxKoltuk.addItem("")
        self.gridLayout.addWidget(self.comboBoxKoltuk, 13, 0, 1, 1)
        self.tableWidgetSeferler = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetSeferler.setObjectName("tableWidgetSeferler")
        self.tableWidgetSeferler.setColumnCount(0)
        self.tableWidgetSeferler.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidgetSeferler, 11, 0, 1, 1)
        self.profilButton = QtWidgets.QPushButton(self.centralwidget)
        self.profilButton.setObjectName("profilButton")
        self.gridLayout.addWidget(self.profilButton, 0, 0, 1, 1)
        self.kalkisNoktasi = QtWidgets.QLineEdit(self.centralwidget)
        self.kalkisNoktasi.setObjectName("kalkisNoktasi")
        self.gridLayout.addWidget(self.kalkisNoktasi, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.seferSorgulaButton = QtWidgets.QPushButton(self.centralwidget)
        self.seferSorgulaButton.setObjectName("seferSorgulaButton")
        self.gridLayout.addWidget(self.seferSorgulaButton, 10, 0, 1, 1)
        self.varisNoktasi = QtWidgets.QLineEdit(self.centralwidget)
        self.varisNoktasi.setObjectName("varisNoktasi")
        self.gridLayout.addWidget(self.varisNoktasi, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 1, 7, 1)
        self.biletAlButton = QtWidgets.QPushButton(self.centralwidget)
        self.biletAlButton.setObjectName("biletAlButton")
        self.gridLayout.addWidget(self.biletAlButton, 14, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 16, 0, 1, 1)
        self.tarih = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.tarih.setDate(QtCore.QDate(2024, 12, 10))
        self.tarih.setTime(QtCore.QTime(8, 0, 0))
        self.tarih.setObjectName("tarih")
        self.gridLayout.addWidget(self.tarih, 9, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 12, 0, 1, 1)
        MainWindowMusAnaEkran.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowMusAnaEkran)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindowMusAnaEkran.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowMusAnaEkran)
        self.statusbar.setObjectName("statusbar")
        MainWindowMusAnaEkran.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowMusAnaEkran)
        QtCore.QMetaObject.connectSlotsByName(MainWindowMusAnaEkran)

    def retranslateUi(self, MainWindowMusAnaEkran):
        _translate = QtCore.QCoreApplication.translate
        MainWindowMusAnaEkran.setWindowTitle(_translate("MainWindowMusAnaEkran", "Müşteri Ana Ekranı"))
        self.comboBoxKoltuk.setItemText(0, _translate("MainWindowMusAnaEkran", "1"))
        self.comboBoxKoltuk.setItemText(1, _translate("MainWindowMusAnaEkran", "2"))
        self.comboBoxKoltuk.setItemText(2, _translate("MainWindowMusAnaEkran", "3"))
        self.comboBoxKoltuk.setItemText(3, _translate("MainWindowMusAnaEkran", "4"))
        self.comboBoxKoltuk.setItemText(4, _translate("MainWindowMusAnaEkran", "5"))
        self.comboBoxKoltuk.setItemText(5, _translate("MainWindowMusAnaEkran", "6"))
        self.comboBoxKoltuk.setItemText(6, _translate("MainWindowMusAnaEkran", "7"))
        self.comboBoxKoltuk.setItemText(7, _translate("MainWindowMusAnaEkran", "8"))
        self.comboBoxKoltuk.setItemText(8, _translate("MainWindowMusAnaEkran", "9"))
        self.comboBoxKoltuk.setItemText(9, _translate("MainWindowMusAnaEkran", "10"))
        self.comboBoxKoltuk.setItemText(10, _translate("MainWindowMusAnaEkran", "11"))
        self.comboBoxKoltuk.setItemText(11, _translate("MainWindowMusAnaEkran", "12"))
        self.comboBoxKoltuk.setItemText(12, _translate("MainWindowMusAnaEkran", "13"))
        self.comboBoxKoltuk.setItemText(13, _translate("MainWindowMusAnaEkran", "14"))
        self.comboBoxKoltuk.setItemText(14, _translate("MainWindowMusAnaEkran", "15"))
        self.comboBoxKoltuk.setItemText(15, _translate("MainWindowMusAnaEkran", "16"))
        self.comboBoxKoltuk.setItemText(16, _translate("MainWindowMusAnaEkran", "17"))
        self.comboBoxKoltuk.setItemText(17, _translate("MainWindowMusAnaEkran", "18"))
        self.comboBoxKoltuk.setItemText(18, _translate("MainWindowMusAnaEkran", "19"))
        self.comboBoxKoltuk.setItemText(19, _translate("MainWindowMusAnaEkran", "20"))
        self.comboBoxKoltuk.setItemText(20, _translate("MainWindowMusAnaEkran", "21"))
        self.comboBoxKoltuk.setItemText(21, _translate("MainWindowMusAnaEkran", "22"))
        self.comboBoxKoltuk.setItemText(22, _translate("MainWindowMusAnaEkran", "23"))
        self.comboBoxKoltuk.setItemText(23, _translate("MainWindowMusAnaEkran", "24"))
        self.comboBoxKoltuk.setItemText(24, _translate("MainWindowMusAnaEkran", "25"))
        self.comboBoxKoltuk.setItemText(25, _translate("MainWindowMusAnaEkran", "26"))
        self.comboBoxKoltuk.setItemText(26, _translate("MainWindowMusAnaEkran", "27"))
        self.comboBoxKoltuk.setItemText(27, _translate("MainWindowMusAnaEkran", "28"))
        self.comboBoxKoltuk.setItemText(28, _translate("MainWindowMusAnaEkran", "29"))
        self.comboBoxKoltuk.setItemText(29, _translate("MainWindowMusAnaEkran", "30"))
        self.comboBoxKoltuk.setItemText(30, _translate("MainWindowMusAnaEkran", "31"))
        self.comboBoxKoltuk.setItemText(31, _translate("MainWindowMusAnaEkran", "32"))
        self.comboBoxKoltuk.setItemText(32, _translate("MainWindowMusAnaEkran", "33"))
        self.comboBoxKoltuk.setItemText(33, _translate("MainWindowMusAnaEkran", "34"))
        self.comboBoxKoltuk.setItemText(34, _translate("MainWindowMusAnaEkran", "35"))
        self.comboBoxKoltuk.setItemText(35, _translate("MainWindowMusAnaEkran", "36"))
        self.comboBoxKoltuk.setItemText(36, _translate("MainWindowMusAnaEkran", "37"))
        self.comboBoxKoltuk.setItemText(37, _translate("MainWindowMusAnaEkran", "38"))
        self.comboBoxKoltuk.setItemText(38, _translate("MainWindowMusAnaEkran", "39"))
        self.comboBoxKoltuk.setItemText(39, _translate("MainWindowMusAnaEkran", "40"))
        self.profilButton.setText(_translate("MainWindowMusAnaEkran", "Profil"))
        self.kalkisNoktasi.setText(_translate("MainWindowMusAnaEkran", "İstanbul"))
        self.label_6.setText(_translate("MainWindowMusAnaEkran", "Varış Noktası Seçiniz"))
        self.seferSorgulaButton.setText(_translate("MainWindowMusAnaEkran", "Sefer Sorgula"))
        self.varisNoktasi.setText(_translate("MainWindowMusAnaEkran", "Ankara"))
        self.biletAlButton.setText(_translate("MainWindowMusAnaEkran", "Bileti al"))
        self.label_5.setText(_translate("MainWindowMusAnaEkran", "Kalkış Noktası Seçiniz"))
        self.label_7.setText(_translate("MainWindowMusAnaEkran", "Tarih Seçiniz"))
        self.label_2.setText(_translate("MainWindowMusAnaEkran", "Koltuk seç"))