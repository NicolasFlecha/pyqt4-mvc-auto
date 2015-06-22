# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append('../Controladores')
from main_controller import *

class MainWindow (QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.controlador = MainControlador(self)
        self.init_ui()

    def init_ui(self):
        self.label = QtGui.QLabel('Cantidad de Personas')
        h_layout = QtGui.QHBoxLayout()
        h_layout.addWidget(self.label)
        button_subir = QtGui.QPushButton('Subir Persona')
        button_bajar = QtGui.QPushButton('Bajar Persona')
        button_subir5 = QtGui.QPushButton('Subir 5 Personas')
        button_bajar5 = QtGui.QPushButton('Bajar 5 Personas')
        button_subir_varias = QtGui.QPushButton('Subir estas Personas')
        button_bajar_varias = QtGui.QPushButton('Bajar estas Personas')

        self.ingreso_numero = QtGui.QLineEdit(self)


#¿?
#        button_subir_varias = QtGui.QInputDialog('Subir estas Personas')
#        button_bajar_varias = QtGui.QInputDialog('Bajar estas Personas')

        h_layout.addWidget(button_subir)
        h_layout.addWidget(button_bajar)
        h_layout.addWidget(button_bajar5)
        h_layout.addWidget(button_subir5)
        h_layout.addWidget(button_subir_varias)
        h_layout.addWidget(button_bajar_varias)


        button_subir.clicked.connect(self.controlador.handler_subir_persona)
        button_bajar.clicked.connect(self.controlador.handler_bajar_persona)
        button_bajar5.clicked.connect(self.controlador.handler_bajar_persona5)
        button_subir5.clicked.connect(self.controlador.handler_subir_persona5)
        button_subir_varias.clicked.connect(self.controlador.handler_subir_varias_personas)
        button_bajar_varias.clicked.connect(self.controlador.handler_bajar_varias_personas)

        self.setLayout(h_layout)
        self.setWindowTitle('Proyecto del Auto')
        self.setGeometry(300, 300, 300, 300)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
