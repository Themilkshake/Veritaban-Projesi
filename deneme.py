# python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\yer_istasyonu_3.py & python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\video_html\app.py
import sys
from PyQt6.QtGui import QPixmap, QIcon, QColor, QTransform
from openpyxl import Workbook
from giris_UI import Ui_MainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QApplication,QMainWindow
import sys

#------------------------------------------------
SERVER_NAME = 'ALI'
DATABASE_NAME = 'journey_management'
def createConnection():
    connString = f'DRIVER={{SQL Server}};'\
                f'SERVER={SERVER_NAME};'\
                f'DATABASE={DATABASE_NAME}'

    global db
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connString)

    if db.open():
        print('SQL SERVER basarili bir sekilde acildi')
        return True
    else:
        print('SQ SERVER baglanti hatasi')
        return False
#-------------------------------------------------


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #--------------- veri çekme kısmı----------


        #------------------------------------------
    

    def buton_tikla(self):
        pass

    def load_data(self):
        pass
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())
