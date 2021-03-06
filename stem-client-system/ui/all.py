# Form implementation generated from reading ui file 'all.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("display: flex;\n"
"align-items: center;\n"
"justify-content: center;")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 580, 508))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_2 = QtWidgets.QFrame(self.page)
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
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
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
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsDragEnabled|QtCore.Qt.ItemFlag.ItemIsDropEnabled|QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsDragEnabled|QtCore.Qt.ItemFlag.ItemIsDropEnabled|QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsDragEnabled|QtCore.Qt.ItemFlag.ItemIsDropEnabled|QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
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
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionCadastrar_novo_cliente = QtGui.QAction(MainWindow)
        self.actionCadastrar_novo_cliente.setObjectName("actionCadastrar_novo_cliente")
        self.actionListar_clientes_existentes = QtGui.QAction(MainWindow)
        self.actionListar_clientes_existentes.setObjectName("actionListar_clientes_existentes")
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuMenu.addAction(self.actionCadastrar_novo_cliente)
        self.menuMenu.addAction(self.actionListar_clientes_existentes)
        self.menuMenu.addAction(self.actionSair)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Cadastrar novo cliente"))
        self.input_name_2.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.input_age_2.setPlaceholderText(_translate("MainWindow", "Idade"))
        self.button_create_2.setText(_translate("MainWindow", "Cadastrar"))
        self.label_3.setText(_translate("MainWindow", "Lista de clientes"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Idade"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Kirk"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Teste"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.button_create_3.setText(_translate("MainWindow", "Excluir"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionCadastrar_novo_cliente.setText(_translate("MainWindow", "Cadastrar novo cliente"))
        self.actionListar_clientes_existentes.setText(_translate("MainWindow", "Listar clientes existentes"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
