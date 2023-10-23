# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
class customPlotWidget(pg.PlotWidget):
    def contextMenuEvent(self, event):
        # Get the position of the context manu event
        pos = event.pos()
        
        # Check if the context menu event happened on a plot item
        items = self.scene().items(self.mapToScene(pos))
        
        for item in items:
            if isinstance(item, pg.PlotItem):
                # Create custom context menu for plot item
                custom_menu = QtWidgets.QMenu(self.view_widget)
                
                action_rename = QtWidgets.QAction("Rename", self)
                action_change_color = QtWidgets.QAction("Color", self)
                
                custom_menu.addAction(action_rename)
                custom_menu.addAction(action_change_color)
                
                custom_menu.exec_(self.view_widget.mapToGlobal(pos))
                return
        
        # If the context menu event didn't happen on a plot item, show the default built-in context menu
        super().contextMenuEvent(event)
        

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(908, 488)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.view_widget = customPlotWidget(Form)
        self.view_widget.setObjectName("view_widget")
        self.horizontalLayout.addWidget(self.view_widget)
        self.verticalScrollBar = QtWidgets.QScrollBar(Form)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setInvertedAppearance(True)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalScrollBar = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_view = QtWidgets.QLabel(Form)
        self.lbl_view.setMaximumSize(QtCore.QSize(60, 20))
        self.lbl_view.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_view.setObjectName("lbl_view")
        self.gridLayout.addWidget(self.lbl_view, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.dial_speed = QtWidgets.QDial(Form)
        self.dial_speed.setMinimum(1)
        self.dial_speed.setMaximum(100)
        self.dial_speed.setNotchesVisible(True)
        self.dial_speed.setObjectName("dial_speed")
        self.gridLayout.addWidget(self.dial_speed, 0, 4, 3, 1)
        self.btn_add_signal = QtWidgets.QPushButton(Form)
        self.btn_add_signal.setObjectName("btn_add_signal")
        self.gridLayout.addWidget(self.btn_add_signal, 1, 0, 1, 1)
        self.btn_start_pause = QtWidgets.QPushButton(Form)
        self.btn_start_pause.setObjectName("btn_start_pause")
        self.gridLayout.addWidget(self.btn_start_pause, 1, 1, 1, 1)
        self.btn_zoom_out = QtWidgets.QPushButton(Form)
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        self.gridLayout.addWidget(self.btn_zoom_out, 1, 3, 1, 1)
        self.btn_remove = QtWidgets.QPushButton(Form)
        self.btn_remove.setObjectName("btn_remove")
        self.gridLayout.addWidget(self.btn_remove, 2, 0, 1, 1)
        self.btn_restart = QtWidgets.QPushButton(Form)
        self.btn_restart.setObjectName("btn_restart")
        self.gridLayout.addWidget(self.btn_restart, 2, 1, 1, 1)
        self.btn_snapshot = QtWidgets.QPushButton(Form)
        self.btn_snapshot.setObjectName("btn_snapshot")
        self.gridLayout.addWidget(self.btn_snapshot, 2, 2, 1, 1)
        self.btn_link = QtWidgets.QPushButton(Form)
        self.btn_link.setObjectName("btn_link")
        self.gridLayout.addWidget(self.btn_link, 2, 3, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(Form)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 3, 0, 1, 1)
        self.btn_transfer = QtWidgets.QPushButton(Form)
        self.btn_transfer.setObjectName("btn_transfer")
        self.gridLayout.addWidget(self.btn_transfer, 3, 1, 1, 1)
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 3, 2, 1, 1)
        self.lbl_speed = QtWidgets.QLabel(Form)
        self.lbl_speed.setMinimumSize(QtCore.QSize(101, 0))
        self.lbl_speed.setMaximumSize(QtCore.QSize(60, 20))
        self.lbl_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_speed.setObjectName("lbl_speed")
        self.gridLayout.addWidget(self.lbl_speed, 3, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_zoom_in = QtWidgets.QPushButton(Form)
        self.btn_zoom_in.setIconSize(QtCore.QSize(60, 60))
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.gridLayout.addWidget(self.btn_zoom_in, 1, 2, 1, 1)
        self.btn_change_color = QtWidgets.QPushButton(Form)
        self.btn_change_color.setObjectName("btn_change_color")
        self.gridLayout.addWidget(self.btn_change_color, 3, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_view.setText(_translate("Form", "View"))
        self.btn_add_signal.setText(_translate("Form", "add_signal"))
        self.btn_add_signal.setShortcut(_translate("Form", "Ctrl+O"))
        self.btn_start_pause.setText(_translate("Form", "start/pause"))
        self.btn_start_pause.setShortcut(_translate("Form", "Space"))
        self.btn_zoom_out.setText(_translate("Form", "zoom_out"))
        self.btn_zoom_out.setShortcut(_translate("Form", "Ctrl+Down"))
        self.btn_remove.setText(_translate("Form", "remove"))
        self.btn_restart.setText(_translate("Form", "restart"))
        self.btn_snapshot.setText(_translate("Form", "snapshot"))
        self.btn_link.setText(_translate("Form", "link"))
        self.btn_clear.setText(_translate("Form", "clear"))
        self.btn_transfer.setText(_translate("Form", "move_signal"))
        self.btn_save.setText(_translate("Form", "save"))
        self.lbl_speed.setText(_translate("Form", "Speed"))
        self.btn_zoom_in.setText(_translate("Form", "zoom_in"))
        self.btn_zoom_in.setShortcut(_translate("Form", "Ctrl+Up"))
        self.btn_change_color.setText(_translate("Form", "Color"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
