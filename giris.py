# python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\yer_istasyonu_3.py & python C:\Users\lenovo\Desktop\MEKATEK_MUY\pyqt6_yer_istasyonu\video_html\app.py
import sys
from openpyxl import Workbook
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from giris_UI import Ui_MainWindowGiris


#------------------------------------------------
SERVER_NAME = 'ALI'
DATABASE_NAME = 'journey_management2'
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
#--------------------------------------------------



class Window(QMainWindow, Ui_MainWindowGiris):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.silme_log()
        self.musGirisButton.clicked.connect(self.load_data_mus)
        self.perGirisButton.clicked.connect(self.load_data_per)

    def load_data_per(self):
        # personel için veri çekme kodu
        if createConnection():  # Bağlantı kurulmuyorsa hata gösterin
            query = QSqlQuery(db)
            query.exec_("SELECT firstName FROM Employee")
            results_perAd = []
            while query.next():
                results_perAd.append(query.value("firstName"))


            query.exec_("SELECT employeeID, Password FROM Employee")
            results_perSif = []
            results_perID = []
            while query.next():
                results_perSif.append(query.value("Password"))
                results_perID.append(query.value("employeeID"))


        if db.isOpen():
            db.close()


        perAd=self.perAd.text()
        perSif=self.perSif.text()
        per_Ad_sayac = 0
        giris_kontrol_1=0
        for i in results_perAd:
            print(per_Ad_sayac)
            if i == perAd and results_perSif[per_Ad_sayac] == perSif:

                per_ID = results_perID[per_Ad_sayac]  # Employee ID değerini al

                try:
                    if createConnection():  # Bağlantı kurulumunu kontrol et
                        query = QSqlQuery(db)

                        # Çalışan bilgilerini sorgula
                        query.exec_(f"SELECT * FROM Employee WHERE employeeID = {per_ID}")

                        if query.next():
                            # Çalışan bilgilerini al
                            employeeID = query.value("employeeID")
                            firstName = query.value("firstName")
                            lastName = query.value("lastName")
                            phone = query.value("phone")
                            department = query.value("department")
                            username = query.value("username")
                            password = query.value("Password")
                            authorizationID = query.value("authorizationID")

                            # Veritabanına ekle
                            insert_query = QSqlQuery(db)
                            insert_query.prepare("""
                                INSERT INTO LogEmployee 
                                (employeeID, firstName, lastName, phone, department, username, password, authorizationID)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """)
                            insert_query.addBindValue(employeeID)
                            insert_query.addBindValue(firstName)
                            insert_query.addBindValue(lastName)
                            insert_query.addBindValue(phone)
                            insert_query.addBindValue(department)
                            insert_query.addBindValue(username)
                            insert_query.addBindValue(password)
                            insert_query.addBindValue(authorizationID)

                            if insert_query.exec_():
                                print("Veriler LogEmployee tablosuna başarıyla eklendi.")
                            else:
                                print("Veri ekleme hatası:", insert_query.lastError().text())

                    if db.isOpen():
                        db.close()

                except Exception as ex:
                    print(f"Hata oluştu: {ex}")

                print("giriş başarili")
                self.close()
                #BURAA
                giris_kontrol_1 = 0
                break
            else:
                giris_kontrol_1 = 1
            per_Ad_sayac +=1

        if giris_kontrol_1 == 1:
            QMessageBox.information(None, "Hata", "Kullanıcı adı yada parola hatalı.")



    def load_data_mus(self):
        # musteri için veri çekme kodu
        if createConnection():  # Bağlantı kurulmuyorsa hata gösterin
            query = QSqlQuery(db)
            query.exec_("SELECT firstName FROM Customer")
            results_musAd = []
            while query.next():
                results_musAd.append(query.value("firstName"))


            query.exec_("SELECT customerID, Password FROM Customer")
            results_musSif = []
            results_musID = []
            while query.next():
                results_musSif.append(query.value("Password"))
                results_musID.append(query.value("customerID"))
                
        if db.isOpen():
            db.close()

        #------------------
        musAd=self.musAd.text()
        musSif=self.musSif.text()
        mus_Ad_sayac = 0
        giris_kontrol=0
        for i in results_musAd:
            print(mus_Ad_sayac)
            if i == musAd and results_musSif[mus_Ad_sayac] == musSif:

                mus_ID = results_musID[mus_Ad_sayac]

                try:
                    if createConnection():  # Bağlantı kurulumunu kontrol et
                        query = QSqlQuery(db)

                        # Müşteri bilgilerini sorgula
                        query.exec_(f"SELECT * FROM Customer WHERE customerID = {mus_ID}")

                        if query.next():
                            # Müşteri bilgilerini al
                            customerID = query.value("customerID")
                            firstName = query.value("firstName")
                            lastName = query.value("lastName")
                            phone = query.value("phone")
                            email = query.value("email")
                            password = query.value("Password")
                            tcKimlikNo = query.value("tcKimlikNo")
                            authorizationID = query.value("authorizationID")

                            # Veritabanına ekle
                            insert_query = QSqlQuery(db)
                            insert_query.prepare("""
                                INSERT INTO LogCustomer 
                                (customerID, firstName, lastName, phone, email, password, tcKimlikNo, authorizationID)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """)
                            insert_query.addBindValue(customerID)
                            insert_query.addBindValue(firstName)
                            insert_query.addBindValue(lastName)
                            insert_query.addBindValue(phone)
                            insert_query.addBindValue(email)
                            insert_query.addBindValue(password)
                            insert_query.addBindValue(tcKimlikNo)
                            insert_query.addBindValue(authorizationID)

                            if insert_query.exec_():
                                print("Veriler LogCustomer tablosuna başarıyla eklendi.")
                            else:
                                print("Veri ekleme hatası:", insert_query.lastError().text())

                    if db.isOpen():
                        db.close()

                except Exception as ex:
                    print(f"Hata oluştu: {ex}")


                print("giris başarili")

                self.close()
                
                with open("musteri_ana_ekrani.py", "r") as file:
                    kod = file.read()
                    exec(kod)

                    
                giris_kontrol = 0
                break
            else:
                giris_kontrol = 1
            
            mus_Ad_sayac +=1

        if giris_kontrol == 1:
            QMessageBox.information(None, "Hata", "Kullanıcı adı yada parola hatalı.")
        #********************

    def silme_log(self):
        try:
            if createConnection():  # Bağlantı kurulumunu kontrol et
                query = QSqlQuery(db)

                # LogCustomer tablosunu temizleme sorgusu
                delete_query = "TRUNCATE TABLE LogCustomer"
                if query.exec_(delete_query):
                    print("LogCustomer tablosu başarıyla temizlendi.")
                else:
                    print(f"Silme hatası: {query.lastError().text()}")


                delete_query2 = "TRUNCATE TABLE LogEmployee"
                if query.exec_(delete_query2):
                    print("LogEmployee tablosu başarıyla temizlendi.")
                else:
                    print(f"Silme hatası: {query.lastError().text()}")

            if db.isOpen():
                db.close()

        except Exception as ex:
            print(f"Bilinmeyen bir hata oluştu!\n{ex}")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())
