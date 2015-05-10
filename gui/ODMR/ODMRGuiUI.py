# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ODMRGuiUI.ui'
#
# Created: Fri May 08 11:25:30 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1066, 567)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.odmr_matrix_ViewWidget = PlotWidget(self.centralwidget)
        self.odmr_matrix_ViewWidget.setObjectName(_fromUtf8("odmr_matrix_ViewWidget"))
        self.gridLayout.addWidget(self.odmr_matrix_ViewWidget, 6, 0, 1, 9)
        self.idle_RadioButton = QtGui.QRadioButton(self.centralwidget)
        self.idle_RadioButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.idle_RadioButton.setObjectName(_fromUtf8("idle_RadioButton"))
        self.gridLayout.addWidget(self.idle_RadioButton, 3, 0, 1, 1)
        self.start_freq_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.start_freq_InputWidget.setMaximumSize(QtCore.QSize(75, 16777215))
        self.start_freq_InputWidget.setObjectName(_fromUtf8("start_freq_InputWidget"))
        self.gridLayout.addWidget(self.start_freq_InputWidget, 1, 2, 1, 1)
        self.run_RadioButton = QtGui.QRadioButton(self.centralwidget)
        self.run_RadioButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.run_RadioButton.setObjectName(_fromUtf8("run_RadioButton"))
        self.gridLayout.addWidget(self.run_RadioButton, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.step_freq_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.step_freq_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.step_freq_InputWidget.setObjectName(_fromUtf8("step_freq_InputWidget"))
        self.gridLayout.addWidget(self.step_freq_InputWidget, 1, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)
        self.stop_freq_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.stop_freq_InputWidget.setMaximumSize(QtCore.QSize(75, 16777215))
        self.stop_freq_InputWidget.setObjectName(_fromUtf8("stop_freq_InputWidget"))
        self.gridLayout.addWidget(self.stop_freq_InputWidget, 1, 6, 1, 1)
        self.runtime_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.runtime_InputWidget.setEnabled(True)
        self.runtime_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.runtime_InputWidget.setObjectName(_fromUtf8("runtime_InputWidget"))
        self.gridLayout.addWidget(self.runtime_InputWidget, 3, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.mode_ComboWidget = QtGui.QComboBox(self.centralwidget)
        self.mode_ComboWidget.setObjectName(_fromUtf8("mode_ComboWidget"))
        self.gridLayout.addWidget(self.mode_ComboWidget, 0, 6, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.odmr_ViewWidget = PlotWidget(self.centralwidget)
        self.odmr_ViewWidget.setObjectName(_fromUtf8("odmr_ViewWidget"))
        self.gridLayout.addWidget(self.odmr_ViewWidget, 5, 0, 1, 9)
        self.frequency_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.frequency_InputWidget.setMaximumSize(QtCore.QSize(75, 16777215))
        self.frequency_InputWidget.setObjectName(_fromUtf8("frequency_InputWidget"))
        self.gridLayout.addWidget(self.frequency_InputWidget, 0, 2, 1, 1)
        self.power_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.power_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.power_InputWidget.setObjectName(_fromUtf8("power_InputWidget"))
        self.gridLayout.addWidget(self.power_InputWidget, 0, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 4, 1, 2)
        self.elapsed_time_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.elapsed_time_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.elapsed_time_InputWidget.setObjectName(_fromUtf8("elapsed_time_InputWidget"))
        self.gridLayout.addWidget(self.elapsed_time_InputWidget, 3, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 8, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 7)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Options = QtGui.QMenu(self.menubar)
        self.menu_Options.setObjectName(_fromUtf8("menu_Options"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Settings = QtGui.QAction(MainWindow)
        self.action_Settings.setObjectName(_fromUtf8("action_Settings"))
        self.menu_Options.addAction(self.action_Settings)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Options.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "qudi: ODMR", None, QtGui.QApplication.UnicodeUTF8))
        self.idle_RadioButton.setText(QtGui.QApplication.translate("MainWindow", "Idle", None, QtGui.QApplication.UnicodeUTF8))
        self.run_RadioButton.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Power [dBm] :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Step [MHz] :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Stop [MHz] :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Runtime [s] :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Mode :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Start [MHz] :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Frequency [MHz] :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Elapsed Time [s] :", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Options.setTitle(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Settings.setText(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget