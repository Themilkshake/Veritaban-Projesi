# python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\yer_istasyonu_3.py & python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\video_html\app.py
import sys
from openpyxl import Workbook
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from musteri_profil_ekrani_UI import Ui_MainWindowMusProfil
import pyodbc

# Veritabanı bağlantı bilgilerini buraya girin
conn_string = (
    r'DRIVER={SQL Server};'
    r'SERVER=ALI;'
    r'DATABASE=journey_management2;'
    r'UID=;'
    r'PWD=;'
)


class WindowMusProfilEkrani(QMainWindow, Ui_MainWindowMusProfil):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.yenile()
        self.anaSayfaButton.clicked.connect(self.anasayfa)
        self.yenileButton.clicked.connect(self.yenile)
        #self.perGirisButton.clicked.connect(self.load_data_per)



    def anasayfa(self):
        #BURAYA ANA SAYFA BUTON KODU GELECEK
        self.close()


    def yenile(self):
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()

            cursor.execute("SELECT CustomerID, firstName, lastName, phone, email, password, tcKimlikNo, authorizationID FROM LogCustomer")
            for row in cursor.fetchall():
                self.adSoyadLabel.setText(f"{row.firstName} {row.lastName}")
                self.kimlikNoLabel.setText(f"{row.tcKimlikNo}")
                self.telNoLabel.setText(f"{row.phone}")
                self.mailLabel.setText(f"{row.email}")

        except pyodbc.Error as ex:
            print(ex)

        finally:
            conn.close()
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    winMusProfil = WindowMusProfilEkrani()
    winMusProfil.show()


    sys.exit(app.exec())