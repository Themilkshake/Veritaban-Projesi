# python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\yer_istasyonu_3.py & python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\video_html\app.py
import sys
from PyQt6.QtGui import QPixmap, QIcon, QColor, QTransform
from openpyxl import Workbook
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView, QApplication,QMainWindow
import sys
import pyodbc

# Veritabanı bağlantı bilgilerini buraya girin
conn_string = (
    r'DRIVER={SQL Server};'
    r'SERVER=ALI;'
    r'DATABASE=journey_management2;'
    r'UID=;'
    r'PWD=;'
)

# #--------------------------------------
# try:
#     conn = pyodbc.connect(conn_string)
#     cursor = conn.cursor()

#     # Sorgunu çalıştır
#     cursor.execute("SELECT * FROM Employee")

#     results = cursor.fetchall()
#     print(results)

#     # Sonuçları yazdırma (örnek)
#     for row in results:
#         print(row)

# except pyodbc.Error as ex:
#     print(ex)

# finally:
#     conn.close()
# #----------------------------------


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())
