# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qgistilemillexport.ui'
#
# Created: Sat Apr  7 15:58:21 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QGISTileMillExport(object):
    def setupUi(self, QGISTileMillExport):
        QGISTileMillExport.setObjectName(_fromUtf8("QGISTileMillExport"))
        QGISTileMillExport.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(QGISTileMillExport)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(QGISTileMillExport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QGISTileMillExport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QGISTileMillExport.reject)
        QtCore.QMetaObject.connectSlotsByName(QGISTileMillExport)

    def retranslateUi(self, QGISTileMillExport):
        QGISTileMillExport.setWindowTitle(QtGui.QApplication.translate("QGISTileMillExport", "QGISTileMillExport", None, QtGui.QApplication.UnicodeUTF8))

