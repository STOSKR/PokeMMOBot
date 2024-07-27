import sys
from PySide6.QtWidgets import QApplication
from UIFunc import UIFunc

def main():
    app = QApplication(sys.argv)
    ui_func = UIFunc()
    ui_func.setFixedSize(652, 476)  # Tamaño ajustado según el archivo UIView.ui
    ui_func.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

