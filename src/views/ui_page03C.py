# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/page03C.ui'
#
# Created: Fri Mar 02 15:53:21 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page03C(object):
    def setupUi(self, Page03C):
        Page03C.setObjectName(_fromUtf8("Page03C"))
        Page03C.resize(730, 559)
        Page03C.setMinimumSize(QtCore.QSize(730, 0))
        Page03C.setMaximumSize(QtCore.QSize(730, 16777215))
        Page03C.setWindowTitle(QtGui.QApplication.translate("Page03C", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Page03C.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(Page03C)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Page03C)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setText(QtGui.QApplication.translate("Page03C", "3| PLUS VALUES ET GAINS TAXABLES A 18%", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setProperty("class", QtGui.QApplication.translate("Page03C", "titreA", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Page03C)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setText(QtGui.QApplication.translate("Page03C", "Cessions de valeurs mobilières, de droits sociaux et assimilés taxables à 18 %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Page03C)
        self.label_7.setStyleSheet(_fromUtf8(""))
        self.label_7.setText(QtGui.QApplication.translate("Page03C", "Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(Page03C)
        self.label_12.setMinimumSize(QtCore.QSize(27, 20))
        self.label_12.setMaximumSize(QtCore.QSize(27, 20))
        self.label_12.setStyleSheet(_fromUtf8(""))
        self.label_12.setText(QtGui.QApplication.translate("Page03C", "3VG", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 3, 1, 1)
        self.f3vg = QtGui.QSpinBox(Page03C)
        self.f3vg.setEnabled(True)
        self.f3vg.setMinimumSize(QtCore.QSize(60, 20))
        self.f3vg.setMaximumSize(QtCore.QSize(60, 20))
        self.f3vg.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f3vg.setWrapping(False)
        self.f3vg.setFrame(True)
        self.f3vg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f3vg.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f3vg.setAccelerated(False)
        self.f3vg.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f3vg.setKeyboardTracking(True)
        self.f3vg.setSuffix(_fromUtf8(""))
        self.f3vg.setPrefix(_fromUtf8(""))
        self.f3vg.setMinimum(0)
        self.f3vg.setMaximum(999999)
        self.f3vg.setSingleStep(1000)
        self.f3vg.setProperty("value", 0)
        self.f3vg.setObjectName(_fromUtf8("f3vg"))
        self.gridLayout.addWidget(self.f3vg, 0, 4, 1, 1)
        self.label_9 = QtGui.QLabel(Page03C)
        self.label_9.setStyleSheet(_fromUtf8(""))
        self.label_9.setText(QtGui.QApplication.translate("Page03C", "Pertes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 5, 1, 1)
        self.label_13 = QtGui.QLabel(Page03C)
        self.label_13.setMinimumSize(QtCore.QSize(27, 20))
        self.label_13.setMaximumSize(QtCore.QSize(27, 20))
        self.label_13.setStyleSheet(_fromUtf8(""))
        self.label_13.setText(QtGui.QApplication.translate("Page03C", "3VH", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 0, 6, 1, 1)
        self.f3vh = QtGui.QSpinBox(Page03C)
        self.f3vh.setEnabled(True)
        self.f3vh.setMinimumSize(QtCore.QSize(60, 20))
        self.f3vh.setMaximumSize(QtCore.QSize(60, 20))
        self.f3vh.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f3vh.setWrapping(False)
        self.f3vh.setFrame(True)
        self.f3vh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f3vh.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f3vh.setAccelerated(False)
        self.f3vh.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f3vh.setKeyboardTracking(True)
        self.f3vh.setSuffix(_fromUtf8(""))
        self.f3vh.setPrefix(_fromUtf8(""))
        self.f3vh.setMinimum(0)
        self.f3vh.setMaximum(999999)
        self.f3vh.setSingleStep(1000)
        self.f3vh.setProperty("value", 0)
        self.f3vh.setObjectName(_fromUtf8("f3vh"))
        self.gridLayout.addWidget(self.f3vh, 0, 7, 1, 1)
        self.label_3 = QtGui.QLabel(Page03C)
        self.label_3.setStyleSheet(_fromUtf8(""))
        self.label_3.setText(QtGui.QApplication.translate("Page03C", "Gains de cession soumis aux prélèvements sociaux.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(Page03C)
        self.label_10.setStyleSheet(_fromUtf8(""))
        self.label_10.setText(QtGui.QApplication.translate("Page03C", "Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_15 = QtGui.QLabel(Page03C)
        self.label_15.setMinimumSize(QtCore.QSize(27, 20))
        self.label_15.setMaximumSize(QtCore.QSize(27, 20))
        self.label_15.setStyleSheet(_fromUtf8(""))
        self.label_15.setText(QtGui.QApplication.translate("Page03C", "3VT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 1, 3, 1, 1)
        self.f3vt = QtGui.QSpinBox(Page03C)
        self.f3vt.setEnabled(True)
        self.f3vt.setMinimumSize(QtCore.QSize(60, 20))
        self.f3vt.setMaximumSize(QtCore.QSize(60, 20))
        self.f3vt.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f3vt.setWrapping(False)
        self.f3vt.setFrame(True)
        self.f3vt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f3vt.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f3vt.setAccelerated(False)
        self.f3vt.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f3vt.setKeyboardTracking(True)
        self.f3vt.setSuffix(_fromUtf8(""))
        self.f3vt.setPrefix(_fromUtf8(""))
        self.f3vt.setMinimum(0)
        self.f3vt.setMaximum(999999)
        self.f3vt.setSingleStep(1000)
        self.f3vt.setProperty("value", 0)
        self.f3vt.setObjectName(_fromUtf8("f3vt"))
        self.gridLayout.addWidget(self.f3vt, 1, 4, 1, 1)
        self.label_11 = QtGui.QLabel(Page03C)
        self.label_11.setStyleSheet(_fromUtf8(""))
        self.label_11.setText(QtGui.QApplication.translate("Page03C", "Pertes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 1, 5, 1, 1)
        self.label_16 = QtGui.QLabel(Page03C)
        self.label_16.setMinimumSize(QtCore.QSize(27, 20))
        self.label_16.setMaximumSize(QtCore.QSize(27, 20))
        self.label_16.setStyleSheet(_fromUtf8(""))
        self.label_16.setText(QtGui.QApplication.translate("Page03C", "3VU", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 1, 6, 1, 1)
        self.f3vu = QtGui.QSpinBox(Page03C)
        self.f3vu.setEnabled(True)
        self.f3vu.setMinimumSize(QtCore.QSize(60, 20))
        self.f3vu.setMaximumSize(QtCore.QSize(60, 20))
        self.f3vu.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f3vu.setWrapping(False)
        self.f3vu.setFrame(True)
        self.f3vu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f3vu.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f3vu.setAccelerated(False)
        self.f3vu.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f3vu.setKeyboardTracking(True)
        self.f3vu.setSuffix(_fromUtf8(""))
        self.f3vu.setPrefix(_fromUtf8(""))
        self.f3vu.setMinimum(0)
        self.f3vu.setMaximum(999999)
        self.f3vu.setSingleStep(1000)
        self.f3vu.setProperty("value", 0)
        self.f3vu.setObjectName(_fromUtf8("f3vu"))
        self.gridLayout.addWidget(self.f3vu, 1, 7, 1, 1)
        self.label_4 = QtGui.QLabel(Page03C)
        self.label_4.setStyleSheet(_fromUtf8(""))
        self.label_4.setText(QtGui.QApplication.translate("Page03C", "Pertes ouvrant droit au crédit d’impôt de 19 %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.label_19 = QtGui.QLabel(Page03C)
        self.label_19.setMinimumSize(QtCore.QSize(27, 20))
        self.label_19.setMaximumSize(QtCore.QSize(27, 20))
        self.label_19.setStyleSheet(_fromUtf8(""))
        self.label_19.setText(QtGui.QApplication.translate("Page03C", "3VV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 2, 6, 1, 1)
        self.f3vv = QtGui.QSpinBox(Page03C)
        self.f3vv.setEnabled(True)
        self.f3vv.setMinimumSize(QtCore.QSize(60, 20))
        self.f3vv.setMaximumSize(QtCore.QSize(60, 20))
        self.f3vv.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f3vv.setWrapping(False)
        self.f3vv.setFrame(True)
        self.f3vv.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f3vv.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f3vv.setAccelerated(False)
        self.f3vv.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f3vv.setKeyboardTracking(True)
        self.f3vv.setSuffix(_fromUtf8(""))
        self.f3vv.setPrefix(_fromUtf8(""))
        self.f3vv.setMinimum(0)
        self.f3vv.setMaximum(999999)
        self.f3vv.setSingleStep(1000)
        self.f3vv.setProperty("value", 0)
        self.f3vv.setObjectName(_fromUtf8("f3vv"))
        self.gridLayout.addWidget(self.f3vv, 2, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_5 = QtGui.QLabel(Page03C)
        self.label_5.setStyleSheet(_fromUtf8(""))
        self.label_5.setText(QtGui.QApplication.translate("Page03C", "4| REVENUS FONCIERS lignes BA, BB, BC, BD", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setProperty("class", QtGui.QApplication.translate("Page03C", "titreA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_36 = QtGui.QLabel(Page03C)
        self.label_36.setStyleSheet(_fromUtf8(""))
        self.label_36.setText(QtGui.QApplication.translate("Page03C", "report du résultat déterminé sur la déclaration n° 2044", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.verticalLayout.addWidget(self.label_36)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_26 = QtGui.QLabel(Page03C)
        self.label_26.setStyleSheet(_fromUtf8(""))
        self.label_26.setText(QtGui.QApplication.translate("Page03C", "Micro foncier : recettes brutes sans abattement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.label_27 = QtGui.QLabel(Page03C)
        self.label_27.setMinimumSize(QtCore.QSize(27, 20))
        self.label_27.setMaximumSize(QtCore.QSize(27, 20))
        self.label_27.setStyleSheet(_fromUtf8(""))
        self.label_27.setText(QtGui.QApplication.translate("Page03C", "4BE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.f4be = QtGui.QSpinBox(Page03C)
        self.f4be.setEnabled(True)
        self.f4be.setMinimumSize(QtCore.QSize(60, 20))
        self.f4be.setMaximumSize(QtCore.QSize(60, 20))
        self.f4be.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f4be.setWrapping(False)
        self.f4be.setFrame(True)
        self.f4be.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f4be.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f4be.setAccelerated(False)
        self.f4be.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f4be.setKeyboardTracking(True)
        self.f4be.setSuffix(_fromUtf8(""))
        self.f4be.setPrefix(_fromUtf8(""))
        self.f4be.setMinimum(0)
        self.f4be.setMaximum(999999)
        self.f4be.setSingleStep(1000)
        self.f4be.setProperty("value", 0)
        self.f4be.setObjectName(_fromUtf8("f4be"))
        self.gridLayout_2.addWidget(self.f4be, 0, 3, 1, 2)
        self.label_28 = QtGui.QLabel(Page03C)
        self.label_28.setStyleSheet(_fromUtf8(""))
        self.label_28.setText(QtGui.QApplication.translate("Page03C", "Revenus fonciers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_2.addWidget(self.label_28, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 1, 1, 1)
        self.label_29 = QtGui.QLabel(Page03C)
        self.label_29.setMinimumSize(QtCore.QSize(27, 20))
        self.label_29.setMaximumSize(QtCore.QSize(27, 20))
        self.label_29.setStyleSheet(_fromUtf8(""))
        self.label_29.setText(QtGui.QApplication.translate("Page03C", "4BA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_2.addWidget(self.label_29, 1, 2, 1, 1)
        self.f4ba = QtGui.QSpinBox(Page03C)
        self.f4ba.setEnabled(True)
        self.f4ba.setMinimumSize(QtCore.QSize(60, 20))
        self.f4ba.setMaximumSize(QtCore.QSize(60, 20))
        self.f4ba.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f4ba.setWrapping(False)
        self.f4ba.setFrame(True)
        self.f4ba.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f4ba.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f4ba.setAccelerated(False)
        self.f4ba.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f4ba.setKeyboardTracking(True)
        self.f4ba.setSuffix(_fromUtf8(""))
        self.f4ba.setPrefix(_fromUtf8(""))
        self.f4ba.setMinimum(0)
        self.f4ba.setMaximum(999999)
        self.f4ba.setSingleStep(1000)
        self.f4ba.setProperty("value", 0)
        self.f4ba.setObjectName(_fromUtf8("f4ba"))
        self.gridLayout_2.addWidget(self.f4ba, 1, 3, 1, 2)
        self.label_24 = QtGui.QLabel(Page03C)
        self.label_24.setStyleSheet(_fromUtf8(""))
        self.label_24.setText(QtGui.QApplication.translate("Page03C", "Déficit imputable sur les revenus fonciers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        self.label_25 = QtGui.QLabel(Page03C)
        self.label_25.setMinimumSize(QtCore.QSize(27, 20))
        self.label_25.setMaximumSize(QtCore.QSize(27, 20))
        self.label_25.setStyleSheet(_fromUtf8(""))
        self.label_25.setText(QtGui.QApplication.translate("Page03C", "4BB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_2.addWidget(self.label_25, 2, 2, 1, 1)
        self.f4bb = QtGui.QSpinBox(Page03C)
        self.f4bb.setEnabled(True)
        self.f4bb.setMinimumSize(QtCore.QSize(60, 20))
        self.f4bb.setMaximumSize(QtCore.QSize(60, 20))
        self.f4bb.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f4bb.setWrapping(False)
        self.f4bb.setFrame(True)
        self.f4bb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f4bb.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f4bb.setAccelerated(False)
        self.f4bb.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f4bb.setKeyboardTracking(True)
        self.f4bb.setSuffix(_fromUtf8(""))
        self.f4bb.setPrefix(_fromUtf8(""))
        self.f4bb.setMinimum(0)
        self.f4bb.setMaximum(999999)
        self.f4bb.setSingleStep(1000)
        self.f4bb.setProperty("value", 0)
        self.f4bb.setObjectName(_fromUtf8("f4bb"))
        self.gridLayout_2.addWidget(self.f4bb, 2, 3, 1, 2)
        self.label_22 = QtGui.QLabel(Page03C)
        self.label_22.setStyleSheet(_fromUtf8(""))
        self.label_22.setText(QtGui.QApplication.translate("Page03C", "Déficit imputable sur le revenu global", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_2.addWidget(self.label_22, 3, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 1, 1, 1)
        self.label_23 = QtGui.QLabel(Page03C)
        self.label_23.setMinimumSize(QtCore.QSize(27, 20))
        self.label_23.setMaximumSize(QtCore.QSize(27, 20))
        self.label_23.setStyleSheet(_fromUtf8(""))
        self.label_23.setText(QtGui.QApplication.translate("Page03C", "4BC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_2.addWidget(self.label_23, 3, 2, 1, 1)
        self.f4bc = QtGui.QSpinBox(Page03C)
        self.f4bc.setEnabled(True)
        self.f4bc.setMinimumSize(QtCore.QSize(60, 20))
        self.f4bc.setMaximumSize(QtCore.QSize(60, 20))
        self.f4bc.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f4bc.setWrapping(False)
        self.f4bc.setFrame(True)
        self.f4bc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f4bc.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f4bc.setAccelerated(False)
        self.f4bc.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f4bc.setKeyboardTracking(True)
        self.f4bc.setSuffix(_fromUtf8(""))
        self.f4bc.setPrefix(_fromUtf8(""))
        self.f4bc.setMinimum(0)
        self.f4bc.setMaximum(999999)
        self.f4bc.setSingleStep(1000)
        self.f4bc.setProperty("value", 0)
        self.f4bc.setObjectName(_fromUtf8("f4bc"))
        self.gridLayout_2.addWidget(self.f4bc, 3, 3, 1, 2)
        self.label_30 = QtGui.QLabel(Page03C)
        self.label_30.setStyleSheet(_fromUtf8(""))
        self.label_30.setText(QtGui.QApplication.translate("Page03C", "Déficits antérieurs non encore imputés", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_2.addWidget(self.label_30, 4, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 1, 1, 1)
        self.label_31 = QtGui.QLabel(Page03C)
        self.label_31.setMinimumSize(QtCore.QSize(27, 20))
        self.label_31.setMaximumSize(QtCore.QSize(27, 20))
        self.label_31.setStyleSheet(_fromUtf8(""))
        self.label_31.setText(QtGui.QApplication.translate("Page03C", "4BD", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_2.addWidget(self.label_31, 4, 2, 1, 1)
        self.f4bd = QtGui.QSpinBox(Page03C)
        self.f4bd.setEnabled(True)
        self.f4bd.setMinimumSize(QtCore.QSize(60, 20))
        self.f4bd.setMaximumSize(QtCore.QSize(60, 20))
        self.f4bd.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f4bd.setWrapping(False)
        self.f4bd.setFrame(True)
        self.f4bd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f4bd.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f4bd.setAccelerated(False)
        self.f4bd.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f4bd.setKeyboardTracking(True)
        self.f4bd.setSuffix(_fromUtf8(""))
        self.f4bd.setPrefix(_fromUtf8(""))
        self.f4bd.setMinimum(0)
        self.f4bd.setMaximum(999999)
        self.f4bd.setSingleStep(1000)
        self.f4bd.setProperty("value", 0)
        self.f4bd.setObjectName(_fromUtf8("f4bd"))
        self.gridLayout_2.addWidget(self.f4bd, 4, 3, 1, 2)
        self.label_32 = QtGui.QLabel(Page03C)
        self.label_32.setStyleSheet(_fromUtf8(""))
        self.label_32.setText(QtGui.QApplication.translate("Page03C", "Primes d’assurance des loyers impayés voir notice", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_2.addWidget(self.label_32, 5, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 5, 1, 1, 1)
        self.label_33 = QtGui.QLabel(Page03C)
        self.label_33.setMinimumSize(QtCore.QSize(27, 20))
        self.label_33.setMaximumSize(QtCore.QSize(27, 20))
        self.label_33.setStyleSheet(_fromUtf8(""))
        self.label_33.setText(QtGui.QApplication.translate("Page03C", "4BF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setProperty("class", QtGui.QApplication.translate("Page03C", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_2.addWidget(self.label_33, 5, 2, 1, 1)
        self.f4bf = QtGui.QSpinBox(Page03C)
        self.f4bf.setEnabled(True)
        self.f4bf.setMinimumSize(QtCore.QSize(60, 20))
        self.f4bf.setMaximumSize(QtCore.QSize(60, 20))
        self.f4bf.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f4bf.setWrapping(False)
        self.f4bf.setFrame(True)
        self.f4bf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f4bf.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f4bf.setAccelerated(False)
        self.f4bf.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f4bf.setKeyboardTracking(True)
        self.f4bf.setSuffix(_fromUtf8(""))
        self.f4bf.setPrefix(_fromUtf8(""))
        self.f4bf.setMinimum(0)
        self.f4bf.setMaximum(999999)
        self.f4bf.setSingleStep(1000)
        self.f4bf.setProperty("value", 0)
        self.f4bf.setObjectName(_fromUtf8("f4bf"))
        self.gridLayout_2.addWidget(self.f4bf, 5, 3, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem9 = QtGui.QSpacerItem(20, 112, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)

        self.retranslateUi(Page03C)
        QtCore.QMetaObject.connectSlotsByName(Page03C)

    def retranslateUi(self, Page03C):
        pass

