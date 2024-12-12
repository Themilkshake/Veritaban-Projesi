#from PyQt4 import uic

from PyQt5 import uic

with open('personel_ana_ekrani_UI.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('personel_ana_ekrani_UI.ui', fout)