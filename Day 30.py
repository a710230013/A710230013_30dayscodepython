from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Kalkulator Sederhana')

        self.first_number = QLineEdit()
        self.second_number = QLineEdit()

        self.labelinput1 = QLabel("Masukkan Angka 1")
        self.labelinput2 = QLabel("Masukkan Angka 2")
        self.hasil_label = QLabel("Hasil Perhitungan ")
        self.result_label = QLabel()

        self.add_button = QPushButton('Tambah')
        self.subtract_button = QPushButton('Kurang')
        self.multiply_button = QPushButton('Kali')
        self.divide_button = QPushButton('Bagi')
        self.modulus_button = QPushButton('Modulus')
        self.power_button = QPushButton('Pangkat')

        self.add_button.clicked.connect(self.add_numbers)
        self.subtract_button.clicked.connect(self.subtract_numbers)
        self.multiply_button.clicked.connect(self.multiply_numbers)
        self.divide_button.clicked.connect(self.divide_numbers)
        self.modulus_button.clicked.connect(self.modulus_operation)
        self.power_button.clicked.connect(self.power_operation)

        layout = QVBoxLayout()
        layout.addWidget(self.labelinput1)
        layout.addWidget(self.first_number)
        layout.addWidget(self.labelinput2)
        layout.addWidget(self.second_number)
        layout.addWidget(self.add_button)
        layout.addWidget(self.subtract_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.divide_button)
        layout.addWidget(self.modulus_button)
        layout.addWidget(self.power_button)
        layout.addWidget(self.hasil_label)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_numbers(self):
        result = float(self.first_number.text()) + float(self.second_number.text())
        self.result_label.setText(str(result))

    def subtract_numbers(self):
        result = float(self.first_number.text()) - float(self.second_number.text())
        self.result_label.setText(str(result))

    def multiply_numbers(self):
        result = float(self.first_number.text()) * float(self.second_number.text())
        self.result_label.setText(str(result))

    def divide_numbers(self):
        result = float(self.first_number.text()) / float(self.second_number.text())
        self.result_label.setText(str(result))

    def modulus_operation(self):
        try:
            result = int(self.first_number.text()) % int(self.second_number.text())
            self.result_label.setText(str(result))
        except ValueError:
            self.result_label.setText("Masukan Angka Integer")

    def power_operation(self):
        try:
            base = float(self.first_number.text())
            exponent = float(self.second_number.text())
            result = base ** exponent
            self.result_label.setText(str(result))
        except ValueError:
            self.result_label.setText("Masukan Angka")

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()