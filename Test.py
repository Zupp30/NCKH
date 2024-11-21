from PyQt5 import QtCore, QtGui
from demoUI_Form import Ui_Form
from PyQt5.QtWidgets import *

class TEST(Ui_Form):
    def __init__(self):
        self.setupUi(Form)

        #---------------------
        # Setting up icon
        #---------------------
        myicon = QtGui.QIcon('Icon.png')
        Form.setWindowIcon(myicon)     

        #---------------------
        #This is MessageBox named About
        #---------------------
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(myicon)
        msg.setText("Chương trình được xây dựng bởi nhóm NCKH thầy Chiến - KMA")
        msg.setWindowTitle("About")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.NewButton.clicked.connect(self.NewButtonHandle)

    #---------------------
    # NewButtonHandle goes here
    #---------------------
    def NewButtonHandle(self):
        try:
            self.path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "*.txt")
            text_file = open(self.path, 'r')
            self.Output.setText(text_file.read())
            text_file.close()
        except:
            pass

    #---------------------
    # GoButtonHandle goes here
    #---------------------

    #---------------------
    # PreviousButtonHandle goes here
    #---------------------


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = TEST()
    Form.show()
    sys.exit(app.exec_())