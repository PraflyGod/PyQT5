#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
ZetCode PyQt5 tutorial
 
This program centers a window
on the screen.
 
author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""
 
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
	QDesktopWidget, QPushButton, QApplication,
	QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        self.resize(250, 150)
        self.setWindowTitle('WeiXin')       
        self.setWindowIcon(QIcon('./mm.png')) 
        self.center()

        self.setToolTip('This is a <b>WeiXin</b> main widget')
         
        btn = QPushButton('quit', self)
        btn.setToolTip('This is a <b>quit</b> widget')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.myClose)

        self.show()
         
         
    def center(self):
         
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def myClose(self):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()
        else:
            QCoreApplication.instance().quit()
        	
    def closeEvent(self, event):
         
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())