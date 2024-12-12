from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # QTabWidget oluştur
        self.tabWidget = QTabWidget(self)
        self.setCentralWidget(self.tabWidget)

        # Sekmeler oluştur ve ekle
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabWidget.addTab(self.tab1, "Tab 1")
        self.tabWidget.addTab(self.tab2, "Tab 2")
        self.tabWidget.addTab(self.tab3, "Tab 3")

        # Tab içeriklerini ayarla
        self.tab1.setLayout(self._create_tab_layout("Tab 1 İçeriği"))
        self.tab2.setLayout(self._create_tab_layout("Tab 2 İçeriği"))
        self.tab3.setLayout(self._create_tab_layout("Tab 3 İçeriği"))

        # İkinci sekmeyi devre dışı bırak
        self.tabWidget.setTabEnabled(1, False)

    def _create_tab_layout(self, text):
        layout = QVBoxLayout()
        label = QLabel(text)
        layout.addWidget(label)
        return layout


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
