from PyQt6 import QtCore, QtGui, QtWidgets
from model.client import Client

class ListClientsWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setEvents()
        self.loadData()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(580, 508)
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 380, 330))
        self.frame_3.setStyleSheet("QFrame{\n"
                                   "    background-color: white;\n"
                                   "    border-radius: 10px\n"
                                   "}\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.widget_5 = QtWidgets.QWidget(self.frame_3)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 380, 70))
        self.widget_5.setStyleSheet("background-color: \"#51b2d9\";\n"
                                    "border-top-right-radius: 10px;\n"
                                    "border-top-left-radius: 10px")
        self.widget_5.setObjectName("widget_5")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 380, 70))
        self.label_3.setStyleSheet("text-transform: uppercase;\n"
                                   "font: 16pt \"Kohne Makina\";\n"
                                   "font-weight: bold;\n"
                                   "color: white")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.widget_6 = QtWidgets.QWidget(self.frame_3)
        self.widget_6.setGeometry(QtCore.QRect(0, 70, 380, 260))
        self.widget_6.setObjectName("widget_6")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_6)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 380, 211))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.button_create_3 = QtWidgets.QPushButton(self.widget_6)
        self.button_create_3.setGeometry(QtCore.QRect(250, 220, 121, 31))
        self.button_create_3.setStyleSheet("QPushButton {\n"
                                           "    text-transform: uppercase;\n"
                                           "    font: 12pt \"Kohne Makina\";\n"
                                           "    color: white;\n"
                                           "    background-color: red;\n"
                                           "    border-style: solid;\n"
                                           "}")
        self.button_create_3.setObjectName("button_create_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setEvents(self):
        self.button_create_3.clicked.connect(self.buttonDeleteEvent)

    def buttonDeleteEvent(self):
        self.deleteClients()

    def deleteClients(self):
        try:
            f = open('./data/clients.txt', 'r')
            lines = f.readlines()
            lines = list(map(lambda x: x.replace('\n', ''), lines))
            f.close()
        except FileNotFoundError:
            f = open('./data/clients.txt', 'w')
            f.close()
            return self.loadData()
        str = ''
        cont = 0
        items = list(map(lambda x: x.row(), self.tableWidget.selectedItems()))
        print(items)
        for i in range(0, len(lines), 2):
            if cont in items:
                cont+=1
                continue
            cont += 1
            str += f'{lines[i]}\n{lines[i+1]}\n'
        f = open('./data/clients.txt', 'w')
        f.write(str)
        f.close()
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle('Sucesso')
        dlg.setText('O campo foi deletado com sucesso!' if len(items) == 1 else 'Os campos foram deletados com sucesso!')
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        dlg.exec()
        self.loadData()


    def loadData(self):
        self.tableWidget.setRowCount(0)
        try:
            f = open('./data/clients.txt', 'r')
            lines = f.readlines()
            lines = list(map(lambda x: x.replace('\n', ''), lines))
            f.close()
        except FileNotFoundError:
            f = open('./data/clients.txt', 'w')
            f.close()
            return self.loadData()
        self.tableWidget.setRowCount(int(len(lines)/2))
        cont = 0
        for i in range(0, len(lines), 2):
            client = Client(name=lines[i], age=lines[i+1], id=cont)
            self.tableWidget.setItem(cont, 0, QtWidgets.QTableWidgetItem(f'{client.id}'))
            self.tableWidget.setItem(cont, 1, QtWidgets.QTableWidgetItem(client.name))
            self.tableWidget.setItem(cont, 2, QtWidgets.QTableWidgetItem(client.age))
            cont += 1


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Lista de clientes"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Idade"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "Kirk"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "Teste"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.button_create_3.setText(_translate("Form", "Excluir"))