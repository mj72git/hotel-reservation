
from PyQt5 import QtCore, QtGui, QtWidgets

from hotel import Ui_Form


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    x=[0,1,2,3,4]
    print(x)
    Form.show()
    sys.exit(app.exec_())
