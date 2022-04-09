from PyQt6.QtWidgets import QApplication
from windows.mainWindow import MainWindow

import sys

app = QApplication(sys.argv)

create_window = MainWindow()
create_window.show()

app.exec()