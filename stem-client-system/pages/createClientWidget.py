from PyQt6 import QtCore, QtWidgets
from model.client import Client

class CreateClientWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setup_events()

    def setupUi(self):
        self.setObjectName("Form")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 380, 330))
        self.frame_2.setStyleSheet("QFrame{\n"
                                   "    background-color: white;\n"
                                   "    border-radius: 10px\n"
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget_3 = QtWidgets.QWidget(self.frame_2)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 380, 70))
        self.widget_3.setStyleSheet("background-color: \"#51b2d9\";\n"
                                    "border-top-right-radius: 10px;\n"
                                    "border-top-left-radius: 10px")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 380, 70))
        self.label_2.setStyleSheet("text-transform: uppercase;\n"
                                   "font: 16pt \"Kohne Makina\";\n"
                                   "font-weight: bold;\n"
                                   "color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget_4 = QtWidgets.QWidget(self.frame_2)
        self.widget_4.setGeometry(QtCore.QRect(0, 70, 380, 260))
        self.widget_4.setObjectName("widget_4")
        self.input_name_2 = QtWidgets.QLineEdit(self.widget_4)
        self.input_name_2.setGeometry(QtCore.QRect(90, 50, 200, 30))
        self.input_name_2.setStyleSheet("QLineEdit{\n"
                                        "    padding: 5px 5px;\n"
                                        "    border-width: 1px;\n"
                                        "    border-style: solid;\n"
                                        "    border-radius: 6px;\n"
                                        "    border-color: #51b2d9\n"
                                        "}")
        self.input_name_2.setText("")
        self.input_name_2.setObjectName("input_name_2")
        self.input_age_2 = QtWidgets.QLineEdit(self.widget_4)
        self.input_age_2.setGeometry(QtCore.QRect(90, 100, 200, 30))
        self.input_age_2.setStyleSheet("QLineEdit{\n"
                                       "    padding: 5px 5px;\n"
                                       "    border-width: 1px;\n"
                                       "    border-style: solid;\n"
                                       "    border-radius: 6px;\n"
                                       "    border-color: #51b2d9;\n"
                                       "}")
        self.input_age_2.setText("")
        self.input_age_2.setObjectName("input_age_2")
        self.button_create_2 = QtWidgets.QPushButton(self.widget_4)
        self.button_create_2.setGeometry(QtCore.QRect(70, 180, 240, 30))
        self.button_create_2.setStyleSheet("QPushButton {\n"
                                           "    text-transform: uppercase;\n"
                                           "    font: 12pt \"Kohne Makina\";\n"
                                           "    color: lblack;\n"
                                           "    background-color: #bfffbf;\n"
                                           "    border-style: solid;\n"
                                           "}")
        self.button_create_2.setObjectName("button_create_2")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_events(self):
        self.button_create_2.clicked.connect(self.event_create_button)

    def event_create_clients(self):
        pass

    def event_create_button(self):
        client = Client(name = self.input_name_2.text(), age = self.input_age_2.text())

        if len(''.join(client.name.split(' '))) == 0 or len(''.join(client.age.split(' '))) == 0:
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle('Erro nos campos')
            dlg.setText('Você deve preencher todos os campos!')
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            dlg.exec()
            return
        try:
            client.age = int(client.age)
            file = open('./data/clients.txt', 'a')
            file.write(f'{client.name}\n{client.age}\n')
            file.close()
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle('Sucesso')
            dlg.setText('Clinte foi cadastrado com sucesso!')
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            dlg.exec()

        except ValueError:
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle('Erro nos campos')
            dlg.setText('O campo idade deve ser um número inteiro!')
            dlg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            dlg.exec()
        finally:
            self.input_age_2.setText('')
            self.input_name_2.setText('')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Cadastrar novo cliente"))
        self.input_name_2.setPlaceholderText(_translate("Form", "Nome"))
        self.input_age_2.setPlaceholderText(_translate("Form", "Idade"))
        self.button_create_2.setText(_translate("Form", "Cadastrar"))