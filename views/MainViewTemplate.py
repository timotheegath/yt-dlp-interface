# Form implementation generated from reading ui file '.\views\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 495)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.URLField = QtWidgets.QLineEdit(parent=self.groupBox)
        self.URLField.setObjectName("URLField")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.URLField)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.groupBox_5)
        self.frame.setMinimumSize(QtCore.QSize(100, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.DestinationLabel = QtWidgets.QLabel(parent=self.groupBox_2)
        self.DestinationLabel.setObjectName("DestinationLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.DestinationLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DestinationPath = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.DestinationPath.setObjectName("DestinationPath")
        self.horizontalLayout_2.addWidget(self.DestinationPath)
        self.ChooseFolderButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.ChooseFolderButton.setObjectName("ChooseFolderButton")
        self.horizontalLayout_2.addWidget(self.ChooseFolderButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)
        self.exporFormattLabel = QtWidgets.QLabel(parent=self.groupBox_2)
        self.exporFormattLabel.setObjectName("exporFormattLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.exporFormattLabel)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.groupBox_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DownloadButton = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.DownloadButton.setObjectName("DownloadButton")
        self.horizontalLayout_3.addWidget(self.DownloadButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.StatusText = QtWidgets.QLabel(parent=self.groupBox_4)
        self.StatusText.setMinimumSize(QtCore.QSize(250, 0))
        self.StatusText.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.StatusText.setWordWrap(True)
        self.StatusText.setObjectName("StatusText")
        self.horizontalLayout_3.addWidget(self.StatusText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.DownloadProgress = QtWidgets.QProgressBar(parent=self.groupBox_4)
        self.DownloadProgress.setMinimumSize(QtCore.QSize(250, 0))
        self.DownloadProgress.setProperty("value", 0)
        self.DownloadProgress.setObjectName("DownloadProgress")
        self.horizontalLayout_3.addWidget(self.DownloadProgress)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 22))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(parent=self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFFMPEG_Path = QtGui.QAction(parent=MainWindow)
        self.actionFFMPEG_Path.setObjectName("actionFFMPEG_Path")
        self.menuOptions.addAction(self.actionFFMPEG_Path)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.label.setBuddy(self.URLField)
        self.label_2.setBuddy(self.lineEdit_2)
        self.DestinationLabel.setBuddy(self.DestinationPath)
        self.exporFormattLabel.setBuddy(self.radioButton)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Input settings"))
        self.label.setText(_translate("MainWindow", "YouTube URL"))
        self.URLField.setPlaceholderText(_translate("MainWindow", "https://youtu.be"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Preview"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Export settings"))
        self.label_2.setText(_translate("MainWindow", "File name"))
        self.lineEdit_2.setText(_translate("MainWindow", "Output"))
        self.DestinationLabel.setText(_translate("MainWindow", "Destination folder"))
        self.ChooseFolderButton.setText(_translate("MainWindow", "Choose folder..."))
        self.exporFormattLabel.setText(_translate("MainWindow", "Export format"))
        self.radioButton.setText(_translate("MainWindow", "MP3"))
        self.DownloadButton.setText(_translate("MainWindow", "Download!"))
        self.StatusText.setText(_translate("MainWindow", "Ready"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionFFMPEG_Path.setText(_translate("MainWindow", "FFMPEG Path"))
