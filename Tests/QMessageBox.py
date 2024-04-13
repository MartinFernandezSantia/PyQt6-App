from PyQt6.QtWidgets import QApplication, QMessageBox

def main():
    app = QApplication([])
    QMessageBox.information(None, "Information", "Hello, this is a message box!")
    app.exec()

if __name__ == "__main__":
    main()
