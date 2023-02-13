from PyQt5 import QtWidgets
from keithley2600 import Keithley2600
from keithleygui import KeithleyGuiApp

app = QtWidgets.QApplication([])

keithley = Keithley2600('TCPIP::169.254.0.1::INSTR')
keithley_gui = KeithleyGuiApp(keithley)
keithley_gui.show()
app.exec()