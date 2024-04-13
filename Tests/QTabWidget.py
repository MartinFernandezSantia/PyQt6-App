from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QLabel

class MyTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabWidget Example")
        tab_widget = QTabWidget()
        tab1 = QLabel("This is tab 1")
        tab2 = QLabel("This is tab 2")
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")
        self.setCentralWidget(tab_widget)

def main():
    app = QApplication([])
    window = MyTabWidget()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
