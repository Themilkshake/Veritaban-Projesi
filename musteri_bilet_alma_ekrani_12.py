# python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\yer_istasyonu_3.py & python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\video_html\app.py
import sys
from openpyxl import Workbook, load_workbook
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox

import pyodbc
from musteri_bilet_alma_ekrani_12_UI import Ui_MainWindow



# Veritabanı bağlantı bilgilerini buraya girin
conn_string = (
    r'DRIVER={SQL Server};'
    r'SERVER=ALI;'
    r'DATABASE=journey_management3;'
    r'UID=;'
    r'PWD=;'
)




class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.musteri_veri_cekme_fonksiyonu

    
    def musteri_veri_cekme_fonksiyonu(self):  
        try:
            # Veritabanına bağlan ve sorguyu çalıştır
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Ticket")
            rows = cursor.fetchall()
            # TableWidget'i temizle
            self.tableWidget.setRowCount(0)

            # Sorgu sonuçlarını TableWidget'e ekle
            for row_number, row_data in enumerate(rows):
                
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):

                    item = QTableWidgetItem(str(data) if data is not None else "") 
                    self.tableWidget.setItem(row_number, column_number, item)
        except pyodbc.Error as ex:
            print("Veritabanı Hatası:", ex)
            QMessageBox.critical(self, "Hata", "Veritabanı bağlantı hatası!")

        finally:
            conn.close()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())
