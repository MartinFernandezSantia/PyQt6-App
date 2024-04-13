from PyQt6.QtWidgets import QApplication, QWizard, QWizardPage, QVBoxLayout, QLabel

class MyWizardPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Page 1")
        layout = QVBoxLayout()
        label = QLabel("This is the first page of the wizard.")
        layout.addWidget(label)
        self.setLayout(layout)

def main():
    app = QApplication([])
    wizard = QWizard()
    page = MyWizardPage()
    wizard.addPage(page)
    wizard.setWindowTitle("Wizard Example")
    wizard.exec()
    app.exec()

if __name__ == "__main__":
    main()
