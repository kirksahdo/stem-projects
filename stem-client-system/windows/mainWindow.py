from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from pages.listClientsWidget import ListClientsWidget
from pages.createClientWidget import CreateClientWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setup_events()
        self.actionCadastrar_novo_cliente.setEnabled(False)
        self.stackedWidget.setCurrentWidget(self.page)

    def setupUi(self):
        self.setObjectName("MainWindow")
        ##self.resize(578, 530)
        self.setFixedSize(380, 350)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("display: flex;\n"
"align-items: center;\n"
"justify-content: center;")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 580, 508))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = CreateClientWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = ListClientsWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.setMenuBar(self.menubar)
        self.actionCadastrar_novo_cliente = QtGui.QAction(self)
        self.actionCadastrar_novo_cliente.setObjectName("actionCadastrar_novo_cliente")
        self.actionListar_clientes_existentes = QtGui.QAction(self)
        self.actionListar_clientes_existentes.setObjectName("actionListar_clientes_existentes")
        self.actionSair = QtGui.QAction(self)
        self.actionSair.setObjectName("actionSair")
        self.menuMenu.addAction(self.actionCadastrar_novo_cliente)
        self.menuMenu.addAction(self.actionListar_clientes_existentes)
        self.menuMenu.addAction(self.actionSair)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_events(self):
        self.actionSair.triggered.connect(self.event_quit_action)
        self.actionListar_clientes_existentes.triggered.connect(self.event_list_clients)
        self.actionCadastrar_novo_cliente.triggered.connect(self.event_create_clients)

    def event_quit_action(self):
        sys.exit()

    def event_list_clients(self):
        self.actionCadastrar_novo_cliente.setEnabled(True)
        self.actionListar_clientes_existentes.setEnabled(False)
        self.page_2.loadData()
        self.stackedWidget.setCurrentWidget(self.page_2)

    def event_create_clients(self):
        self.actionCadastrar_novo_cliente.setEnabled(False)
        self.actionListar_clientes_existentes.setEnabled(True)
        self.stackedWidget.setCurrentWidget(self.page)

    def centerWidgetOnScreen(self, widget):
        centerPoint = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        fg = widget.frameGeometry()
        fg.moveCenter(centerPoint)
        widget.move(fg.topLeft())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Clientes"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionCadastrar_novo_cliente.setText(_translate("MainWindow", "Cadastrar novo cliente"))
        self.actionListar_clientes_existentes.setText(_translate("MainWindow", "Listar clientes existentes"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))