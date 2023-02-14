from PyQt5 import QtWidgets
from keithleygui import KeithleyGuiApp

if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    keithley_gui = KeithleyGuiApp()
    keithley_gui.show()
    app.exec()