import sys

from PyQt5.QtWidgets import (
    #QApplication,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QToolButton,
    QPushButton,
    #QLineEdit,
    QLabel,
    QVBoxLayout,
)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        Dialog.resize(self, 500, 300)
        self.setWindowTitle("Transpose tabs")
        dlgLayout = QVBoxLayout()

        self.semitones = 0

        # Create a layout and add widgets
        layout = QGridLayout()
        
        self.plus = QPushButton('+')
        self.plus.clicked.connect(self.transpose(self.plus.text))

        self.minus = QPushButton('-')
        self.minus.clicked.connect(self.transpose(self.minus.text))

        self.semitoneLabel = QLabel(str(self.semitones))

        layout.addWidget(self.plus, 0, 0)
        layout.addWidget(self.minus, 0, 1)
        layout.addWidget(self.semitoneLabel, 1, 1)

        # Add a button box
        self.ok = QPushButton('Ok')
        #self.ok.setEnabled(False)
        self.cancel = QPushButton('Exit')
        #self.cancel.clicked.connect(self.exitapp)

        layout.addWidget(self.ok, 2,0)
        layout.addWidget(self.cancel, 2,1)

        # Set the layout on the dialog
        dlgLayout.addLayout(layout)
        self.setLayout(dlgLayout)

    def transposeUp(self):
        if self.semitones <= 11:
           self.semitones += 1

    def transposeDown(self):
        if self.semitones >= -11:
            self.semitones -= 1

    def transpose(self, sign):
        if self.plus.isEnabled():
            if sign == '+':
                self.transposeUp()
            else:
                self.transposeDown()
            self.semitoneLabel.setText(str(self.semitones))

    def minusState(self):
        if self.plus.isEnabled():
            self.transposeDown()
            self.semitoneLabel.setText(str(self.semitones))

#app = QApplication(sys.argv)
#dlg = Dialog()
#dlg.show()
#sys.exit(app.exec_())
