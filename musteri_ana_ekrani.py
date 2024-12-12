# python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\yer_istasyonu_3.py & python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\video_html\app.py
import sys
from openpyxl import Workbook
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from musteri_ana_ekrani_UI import Ui_MainWindowMusAnaEkran
import musteri_profil_ekrani
import pyodbc


#------------------------------------------------
# Veritabanı bağlantı bilgilerini buraya girin
conn_string = (
    r'DRIVER={SQL Server};'
    r'SERVER=ALI;'
    r'DATABASE=journey_management2;'
    r'UID=;'
    r'PWD=;'
)
#--------------------------------------------------



class WindowMusAnaEkran(QMainWindow, Ui_MainWindowMusAnaEkran):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.musteri_profil_ekranii = musteri_profil_ekrani.Window()
        #print(girisKimlikk.girisKimlikAd + girisKimlikk.girisKimlikSif)
        self.profilButton.clicked.connect(self.profil_buton)
        self.seferSorgulaButton.clicked.connect(self.load_data_per)
    def profil_buton(self):
        self.close()
        self.musteri_profil_ekranii.show()


    def load_data_per(self):
        try:
            conn = pyodbc.connect(conn_string)
            cursor = conn.cursor()
            if self.kalkisNoktasi.text() and self.varisNoktasi.text():
                # Sorgunu çalıştır
                cursor.execute("SELECT * FROM JOURNEY WHERE departureCity='"+self.kalkisNoktasi.text()+"' AND arrivalCity='"+self.varisNoktasi.text()+"' AND departureDate='"+self.tarih.text()+"'")
                # Sonuçları bir listeye ata
                results = cursor.fetchall()
                print(results)

                # Sonuçları yazdırma (örnek)
                for row in results:
                    print(row)

        except pyodbc.Error as ex:
            print(ex)

        finally:
            conn.close()
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())
