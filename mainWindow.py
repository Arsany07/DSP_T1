# Form implementation generated from reading ui file 'SignalMonitor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Signal_Monitor(object):
    def setupUi(self, Signal_Monitor):
        Signal_Monitor.setObjectName("Signal_Monitor")
        Signal_Monitor.resize(654, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Signal_Monitor.sizePolicy().hasHeightForWidth())
        Signal_Monitor.setSizePolicy(sizePolicy)
        Signal_Monitor.setMinimumSize(QtCore.QSize(640, 500))
        Signal_Monitor.setMaximumSize(QtCore.QSize(1280, 1000))
        self.centralwidget = QtWidgets.QWidget(parent=Signal_Monitor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ControlInfo = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.ControlInfo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ControlInfo.sizePolicy().hasHeightForWidth())
        self.ControlInfo.setSizePolicy(sizePolicy)
        self.ControlInfo.setMinimumSize(QtCore.QSize(200, 0))
        self.ControlInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ControlInfo.setAutoFillBackground(False)
        self.ControlInfo.setReadOnly(True)
        self.ControlInfo.setObjectName("ControlInfo")
        self.gridLayout_3.addWidget(self.ControlInfo, 0, 0, 1, 1)
        self.Signal1 = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Signal1.sizePolicy().hasHeightForWidth())
        self.Signal1.setSizePolicy(sizePolicy)
        self.Signal1.setObjectName("Signal1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Signal1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lyt_Signal = QtWidgets.QGridLayout()
        self.lyt_Signal.setObjectName("lyt_Signal")
        self.lyt_SignalDisplay = QtWidgets.QHBoxLayout()
        self.lyt_SignalDisplay.setObjectName("lyt_SignalDisplay")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.Signal1)
        self.graphicsView.setObjectName("graphicsView")
        self.lyt_SignalDisplay.addWidget(self.graphicsView)
        self.lyt_Signal.addLayout(self.lyt_SignalDisplay, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.lyt_Signal, 3, 0, 1, 1)
        self.ControlLayout = QtWidgets.QGridLayout()
        self.ControlLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.ControlLayout.setContentsMargins(0, -1, -1, -1)
        self.ControlLayout.setObjectName("ControlLayout")
        self.Signal1_Play_Stop = QtWidgets.QPushButton(parent=self.Signal1)
        self.Signal1_Play_Stop.setObjectName("Signal1_Play_Stop")
        self.ControlLayout.addWidget(self.Signal1_Play_Stop, 1, 1, 1, 1)
        self.Signal1_Zoomout = QtWidgets.QPushButton(parent=self.Signal1)
        self.Signal1_Zoomout.setObjectName("Signal1_Zoomout")
        self.ControlLayout.addWidget(self.Signal1_Zoomout, 2, 1, 1, 1)
        self.Signal1_PDF = QtWidgets.QPushButton(parent=self.Signal1)
        self.Signal1_PDF.setObjectName("Signal1_PDF")
        self.ControlLayout.addWidget(self.Signal1_PDF, 2, 2, 1, 1)
        self.Signal1_Zoomin = QtWidgets.QPushButton(parent=self.Signal1)
        self.Signal1_Zoomin.setObjectName("Signal1_Zoomin")
        self.ControlLayout.addWidget(self.Signal1_Zoomin, 2, 0, 1, 1)
        self.Signal1_MovRight = QtWidgets.QPushButton(parent=self.Signal1)
        self.Signal1_MovRight.setObjectName("Signal1_MovRight")
        self.ControlLayout.addWidget(self.Signal1_MovRight, 1, 2, 1, 1)
        self.Signal1_MovLeft = QtWidgets.QPushButton(parent=self.Signal1)
        self.Signal1_MovLeft.setObjectName("Signal1_MovLeft")
        self.ControlLayout.addWidget(self.Signal1_MovLeft, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.ControlLayout, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Signal1, 2, 0, 1, 1)
        self.btn_addView = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_addView.setObjectName("btn_addView")
        self.gridLayout_3.addWidget(self.btn_addView, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        Signal_Monitor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Signal_Monitor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 22))
        self.menubar.setObjectName("menubar")
        self.ActionFile = QtWidgets.QMenu(parent=self.menubar)
        self.ActionFile.setObjectName("ActionFile")
        self.ActionSignal = QtWidgets.QMenu(parent=self.menubar)
        self.ActionSignal.setObjectName("ActionSignal")
        Signal_Monitor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Signal_Monitor)
        self.statusbar.setObjectName("statusbar")
        Signal_Monitor.setStatusBar(self.statusbar)
        self.ActionFile_OpenFile = QtGui.QAction(parent=Signal_Monitor)
        self.ActionFile_OpenFile.setObjectName("ActionFile_OpenFile")
        self.ActionFile_SaveFile = QtGui.QAction(parent=Signal_Monitor)
        self.ActionFile_SaveFile.setObjectName("ActionFile_SaveFile")
        self.ActionFile_ExitFile = QtGui.QAction(parent=Signal_Monitor)
        self.ActionFile_ExitFile.setObjectName("ActionFile_ExitFile")
        self.ActionSignal_LinkSignals = QtGui.QAction(parent=Signal_Monitor)
        self.ActionSignal_LinkSignals.setObjectName("ActionSignal_LinkSignals")
        self.ActionSignal_UnLinkSignals = QtGui.QAction(parent=Signal_Monitor)
        self.ActionSignal_UnLinkSignals.setObjectName("ActionSignal_UnLinkSignals")
        self.ActionFile.addAction(self.ActionFile_OpenFile)
        self.ActionFile.addAction(self.ActionFile_SaveFile)
        self.ActionFile.addSeparator()
        self.ActionFile.addAction(self.ActionFile_ExitFile)
        self.ActionSignal.addAction(self.ActionSignal_LinkSignals)
        self.ActionSignal.addAction(self.ActionSignal_UnLinkSignals)
        self.ActionSignal.addSeparator()
        self.menubar.addAction(self.ActionFile.menuAction())
        self.menubar.addAction(self.ActionSignal.menuAction())

        self.retranslateUi(Signal_Monitor)
        QtCore.QMetaObject.connectSlotsByName(Signal_Monitor)

    def retranslateUi(self, Signal_Monitor):
        _translate = QtCore.QCoreApplication.translate
        Signal_Monitor.setWindowTitle(_translate("Signal_Monitor", "MainWindow"))
        self.ControlInfo.setHtml(_translate("Signal_Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Open New File --&gt; Ctrl+O  |  Save File --&gt; Ctrl+S  |  Exit Program --&gt; Ctrl+X</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pause Signal --&gt; Spacebar |  Mov Signal Right --&gt; Right Arrow | Mov Signal Left --&gt; Left Arrow</span></p></body></html>"))
        self.Signal1.setTitle(_translate("Signal_Monitor", "Signals"))
        self.Signal1_Play_Stop.setText(_translate("Signal_Monitor", "Play"))
        self.Signal1_Play_Stop.setShortcut(_translate("Signal_Monitor", "Space"))
        self.Signal1_Zoomout.setText(_translate("Signal_Monitor", "Zoom out"))
        self.Signal1_PDF.setText(_translate("Signal_Monitor", "PDF"))
        self.Signal1_Zoomin.setText(_translate("Signal_Monitor", "Zoom in"))
        self.Signal1_MovRight.setText(_translate("Signal_Monitor", "Mov Right"))
        self.Signal1_MovRight.setShortcut(_translate("Signal_Monitor", "Right"))
        self.Signal1_MovLeft.setText(_translate("Signal_Monitor", "Mov Left"))
        self.Signal1_MovLeft.setShortcut(_translate("Signal_Monitor", "Left"))
        self.btn_addView.setText(_translate("Signal_Monitor", "Add View"))
        self.ActionFile.setTitle(_translate("Signal_Monitor", "File"))
        self.ActionSignal.setTitle(_translate("Signal_Monitor", "Signal"))
        self.ActionFile_OpenFile.setText(_translate("Signal_Monitor", "Open File             Ctrl+O"))
        self.ActionFile_OpenFile.setShortcut(_translate("Signal_Monitor", "Ctrl+O"))
        self.ActionFile_SaveFile.setText(_translate("Signal_Monitor", "Save File              Ctrl+S"))
        self.ActionFile_SaveFile.setShortcut(_translate("Signal_Monitor", "Ctrl+S"))
        self.ActionFile_ExitFile.setText(_translate("Signal_Monitor", "Exit                      Ctrl+X"))
        self.ActionFile_ExitFile.setShortcut(_translate("Signal_Monitor", "Ctrl+X"))
        self.ActionSignal_LinkSignals.setText(_translate("Signal_Monitor", "Link Signals"))
        self.ActionSignal_UnLinkSignals.setText(_translate("Signal_Monitor", "UnLlink Signals"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signal_Monitor = QtWidgets.QMainWindow()
    ui = Ui_Signal_Monitor()
    ui.setupUi(Signal_Monitor)
    Signal_Monitor.show()
    sys.exit(app.exec())