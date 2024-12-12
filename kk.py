import sys
import pyodbc
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QTextEdit, QComboBox
from PyQt5.QtCore import Qt

class BackupRestoreApp(QWidget):
    def _init_(self):
        super()._init_()

        self.setWindowTitle('SQL Server Geri Yükleme Uygulaması')
        self.setGeometry(100, 100, 600, 400)

        # Layout ve bileşenler
        self.layout = QVBoxLayout()

        self.label = QLabel('Geri Yüklemek için Yedek Dosyasını Seçin:', self)
        self.layout.addWidget(self.label)

        self.select_button = QPushButton('Yedek Dosyasını Seç', self)
        self.select_button.clicked.connect(self.select_backup_file)
        self.layout.addWidget(self.select_button)

        # Veritabanı seçim kutusu (ComboBox)
        self.db_selector_label = QLabel('Geri Yüklenecek Veritabanını Seçin:', self)
        self.layout.addWidget(self.db_selector_label)

        self.db_selector = QComboBox(self)
        self.layout.addWidget(self.db_selector)

        self.restore_button = QPushButton('Geri Yükle', self)
        self.restore_button.clicked.connect(self.restore_database)
        self.layout.addWidget(self.restore_button)

        # İşlem çıktısını gösterecek TextEdit widget'ı
        self.output_box = QTextEdit(self)
        self.output_box.setReadOnly(True)
        self.layout.addWidget(self.output_box)

        self.setLayout(self.layout)

        # Bağlantı parametreleri (localhost üzerinden bağlanma)
        self.conn_str = (
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=localhost;'  # Buraya localhost ya da 127.0.0.1 yazabilirsiniz
            r'DATABASE=master;'  # Bu, master veritabanına bağlanır
            r'Trusted_Connection=yes;'  # Windows Authentication
        )
        self.backup_file = None  # Yedek dosyasının yolu

        # Veritabanlarını yükle
        self.load_databases()

    def load_databases(self):
        """SQL Server'daki veritabanlarını yükleyin ve combobox'a ekleyin."""
        try:
            # SQL Server'a bağlan
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()

            # Mevcut veritabanlarını sorgula
            cursor.execute("SELECT name FROM sys.databases WHERE state_desc = 'ONLINE' AND name NOT IN ('master', 'tempdb', 'model', 'msdb')")
            databases = cursor.fetchall()

            # Veritabanlarını combobox'a ekle
            for db in databases:
                self.db_selector.addItem(db[0])

            cursor.close()
            conn.close()

        except Exception as e:
            self.output_box.append(f"Veritabanları yüklenirken bir hata oluştu: {str(e)}")

    def select_backup_file(self):
        """Kullanıcıdan yedek dosyasını seçmesini isteyin."""
        options = QFileDialog.Options()
        self.backup_file, _ = QFileDialog.getOpenFileName(self, "Yedek Dosyasını Seç", "", "Backup Files (.bak);;All Files ()", options=options)
        if self.backup_file:
            self.label.setText(f"Seçilen Yedek Dosyası: {self.backup_file}")
        else:
            self.label.setText("Yedek dosyası seçilmedi!")

    def restore_database(self):
        """Veritabanını yedek dosyasından geri yükleyin ve ilerlemeyi gösterin."""
        db_name = self.db_selector.currentText()
        if not db_name:
            self.label.setText("Lütfen geçerli bir veritabanı seçin.")
            return

        if not self.backup_file:
            self.label.setText("Lütfen geçerli bir yedek dosyası seçin.")
            return

        try:
            # SQL Server'a bağlan ve autocommit=True yap
            conn = pyodbc.connect(self.conn_str)
            conn.autocommit = True
            cursor = conn.cursor()

            # Geri yükleme komutunu oluştur
            restore_cmd = f"""
            RESTORE DATABASE [{db_name}]
            FROM DISK = N'{self.backup_file}'
            WITH REPLACE,
                 FILE = 1,
                 STATS = 1;  -- Bu komut, her %1'lik ilerlemeyi rapor eder
            """

            # Komut çalıştır
            cursor.execute(restore_cmd)

            # Sonuç kümesini (result set) kontrol et ve işlem ilerlemelerini al
            while cursor.nextset():  # Sonraki küme varsa devam et
                pass

            # Geri yükleme işlemi tamamlandıktan sonra veritabanını MULTI_USER moduna al
            cursor.execute(f"ALTER DATABASE [{db_name}] SET MULTI_USER;")

            # Sonuç mesajlarını ekrana yazdır
            self.output_box.append("Geri yükleme işlemi tamamlandı ve veritabanı MULTI_USER moduna alındı.")
            self.label.setText(f"{db_name} veritabanı başarıyla geri yüklendi ve MULTI_USER moduna alındı.")

            # Bağlantıyı kapat
            cursor.close()
            conn.close()

        except Exception as e:
            # Hata mesajını ekrana yazdır
            self.label.setText(f"Bir hata oluştu: {str(e)}")
            self.output_box.append(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BackupRestoreApp()
    window.show()
    sys.exit(app.exec_())