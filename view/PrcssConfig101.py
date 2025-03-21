# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrcssConfig101.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProcessConf(object):
    def setupUi(self, ProcessConf):
        if not ProcessConf.objectName():
            ProcessConf.setObjectName(u"ProcessConf")
        ProcessConf.resize(1147, 955)
        self.centralwidget = QWidget(ProcessConf)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphLayout = QVBoxLayout()
        self.graphLayout.setObjectName(u"graphLayout")
        self.tab5 = QTabWidget(self.centralwidget)
        self.tab5.setObjectName(u"tab5")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_19 = QVBoxLayout(self.tab_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_graph0 = QVBoxLayout()
        self.verticalLayout_graph0.setObjectName(u"verticalLayout_graph0")

        self.verticalLayout_19.addLayout(self.verticalLayout_graph0)

        self.tab5.addTab(self.tab_6, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_graph1 = QVBoxLayout()
        self.verticalLayout_graph1.setObjectName(u"verticalLayout_graph1")

        self.verticalLayout_6.addLayout(self.verticalLayout_graph1)

        self.tab5.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_graph2 = QVBoxLayout()
        self.verticalLayout_graph2.setObjectName(u"verticalLayout_graph2")

        self.verticalLayout_7.addLayout(self.verticalLayout_graph2)

        self.tab5.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_12 = QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_graph3 = QVBoxLayout()
        self.verticalLayout_graph3.setObjectName(u"verticalLayout_graph3")

        self.verticalLayout_12.addLayout(self.verticalLayout_graph3)

        self.tab5.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_14 = QVBoxLayout(self.tab_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_graph4 = QVBoxLayout()
        self.verticalLayout_graph4.setObjectName(u"verticalLayout_graph4")

        self.verticalLayout_14.addLayout(self.verticalLayout_graph4)

        self.tab5.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_13 = QVBoxLayout(self.tab_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_graph5 = QVBoxLayout()
        self.verticalLayout_graph5.setObjectName(u"verticalLayout_graph5")

        self.verticalLayout_13.addLayout(self.verticalLayout_graph5)

        self.tab5.addTab(self.tab_4, "")

        self.graphLayout.addWidget(self.tab5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.graphLayout.addItem(self.horizontalSpacer)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(16777215, 200))

        self.graphLayout.addWidget(self.textEdit)


        self.horizontalLayout.addLayout(self.graphLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMaximumSize(QSize(450, 16777215))
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.verticalLayout_4 = QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.image_groupBox = QGroupBox(self.stackedWidgetPage1)
        self.image_groupBox.setObjectName(u"image_groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.image_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.image_groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(432, 93))
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.image_groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(150, 3))
        self.label_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_imagpath = QLineEdit(self.image_groupBox)
        self.lineEdit_imagpath.setObjectName(u"lineEdit_imagpath")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_imagpath.sizePolicy().hasHeightForWidth())
        self.lineEdit_imagpath.setSizePolicy(sizePolicy4)
        self.lineEdit_imagpath.setMinimumSize(QSize(200, 0))
        self.lineEdit_imagpath.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_imagpath)

        self.toolButton_imgpath = QToolButton(self.image_groupBox)
        self.toolButton_imgpath.setObjectName(u"toolButton_imgpath")

        self.horizontalLayout_2.addWidget(self.toolButton_imgpath)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.image_groupBox)

        self.Lookuptable_groupBox = QGroupBox(self.stackedWidgetPage1)
        self.Lookuptable_groupBox.setObjectName(u"Lookuptable_groupBox")
        self.verticalLayout_17 = QVBoxLayout(self.Lookuptable_groupBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_20 = QLabel(self.Lookuptable_groupBox)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(432, 93))
        self.label_20.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_20.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_20)

        self.checkBox_lookuptable = QCheckBox(self.Lookuptable_groupBox)
        self.checkBox_lookuptable.setObjectName(u"checkBox_lookuptable")
        self.checkBox_lookuptable.setChecked(False)
        self.checkBox_lookuptable.setTristate(False)

        self.verticalLayout_17.addWidget(self.checkBox_lookuptable)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_21 = QLabel(self.Lookuptable_groupBox)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setMinimumSize(QSize(150, 3))
        self.label_21.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_24.addWidget(self.label_21)

        self.lineEdit_lookuppath = QLineEdit(self.Lookuptable_groupBox)
        self.lineEdit_lookuppath.setObjectName(u"lineEdit_lookuppath")
        sizePolicy4.setHeightForWidth(self.lineEdit_lookuppath.sizePolicy().hasHeightForWidth())
        self.lineEdit_lookuppath.setSizePolicy(sizePolicy4)
        self.lineEdit_lookuppath.setMinimumSize(QSize(200, 0))
        self.lineEdit_lookuppath.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_24.addWidget(self.lineEdit_lookuppath)

        self.toolButton_lookuppath = QToolButton(self.Lookuptable_groupBox)
        self.toolButton_lookuppath.setObjectName(u"toolButton_lookuppath")

        self.horizontalLayout_24.addWidget(self.toolButton_lookuppath)


        self.verticalLayout_17.addLayout(self.horizontalLayout_24)


        self.verticalLayout_4.addWidget(self.Lookuptable_groupBox)

        self.imageExtract_groupBox = QGroupBox(self.stackedWidgetPage1)
        self.imageExtract_groupBox.setObjectName(u"imageExtract_groupBox")
        self.verticalLayout_16 = QVBoxLayout(self.imageExtract_groupBox)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_xscale_3 = QLabel(self.imageExtract_groupBox)
        self.label_xscale_3.setObjectName(u"label_xscale_3")
        self.label_xscale_3.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_3.sizePolicy().hasHeightForWidth())
        self.label_xscale_3.setSizePolicy(sizePolicy3)
        self.label_xscale_3.setMinimumSize(QSize(150, 3))
        self.label_xscale_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_20.addWidget(self.label_xscale_3)

        self.horizontalSpacer_25 = QSpacerItem(54, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.spinBox_extract1_x = QSpinBox(self.imageExtract_groupBox)
        self.spinBox_extract1_x.setObjectName(u"spinBox_extract1_x")
        self.spinBox_extract1_x.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_extract1_x.sizePolicy().hasHeightForWidth())
        self.spinBox_extract1_x.setSizePolicy(sizePolicy2)
        self.spinBox_extract1_x.setMinimumSize(QSize(50, 0))
        self.spinBox_extract1_x.setMinimum(0)
        self.spinBox_extract1_x.setMaximum(10000)
        self.spinBox_extract1_x.setValue(0)

        self.horizontalLayout_20.addWidget(self.spinBox_extract1_x)

        self.label_12 = QLabel(self.imageExtract_groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)

        self.horizontalLayout_20.addWidget(self.label_12)

        self.spinBox_extract1_y = QSpinBox(self.imageExtract_groupBox)
        self.spinBox_extract1_y.setObjectName(u"spinBox_extract1_y")
        self.spinBox_extract1_y.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_extract1_y.sizePolicy().hasHeightForWidth())
        self.spinBox_extract1_y.setSizePolicy(sizePolicy2)
        self.spinBox_extract1_y.setMinimumSize(QSize(50, 0))
        self.spinBox_extract1_y.setMinimum(0)
        self.spinBox_extract1_y.setMaximum(10000)
        self.spinBox_extract1_y.setValue(0)

        self.horizontalLayout_20.addWidget(self.spinBox_extract1_y)

        self.label_13 = QLabel(self.imageExtract_groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)

        self.horizontalLayout_20.addWidget(self.label_13)

        self.horizontalSpacer_26 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_26)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_xscale_9 = QLabel(self.imageExtract_groupBox)
        self.label_xscale_9.setObjectName(u"label_xscale_9")
        self.label_xscale_9.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_9.sizePolicy().hasHeightForWidth())
        self.label_xscale_9.setSizePolicy(sizePolicy3)
        self.label_xscale_9.setMinimumSize(QSize(150, 3))
        self.label_xscale_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_21.addWidget(self.label_xscale_9)

        self.horizontalSpacer_27 = QSpacerItem(54, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)

        self.spinBox_extract2_x = QSpinBox(self.imageExtract_groupBox)
        self.spinBox_extract2_x.setObjectName(u"spinBox_extract2_x")
        self.spinBox_extract2_x.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_extract2_x.sizePolicy().hasHeightForWidth())
        self.spinBox_extract2_x.setSizePolicy(sizePolicy2)
        self.spinBox_extract2_x.setMinimumSize(QSize(50, 0))
        self.spinBox_extract2_x.setMinimum(0)
        self.spinBox_extract2_x.setMaximum(10000)
        self.spinBox_extract2_x.setValue(0)

        self.horizontalLayout_21.addWidget(self.spinBox_extract2_x)

        self.label_14 = QLabel(self.imageExtract_groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy5)

        self.horizontalLayout_21.addWidget(self.label_14)

        self.spinBox_extract2_y = QSpinBox(self.imageExtract_groupBox)
        self.spinBox_extract2_y.setObjectName(u"spinBox_extract2_y")
        self.spinBox_extract2_y.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_extract2_y.sizePolicy().hasHeightForWidth())
        self.spinBox_extract2_y.setSizePolicy(sizePolicy2)
        self.spinBox_extract2_y.setMinimumSize(QSize(50, 0))
        self.spinBox_extract2_y.setMinimum(0)
        self.spinBox_extract2_y.setMaximum(10000)
        self.spinBox_extract2_y.setValue(0)

        self.horizontalLayout_21.addWidget(self.spinBox_extract2_y)

        self.label_17 = QLabel(self.imageExtract_groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)

        self.horizontalLayout_21.addWidget(self.label_17)

        self.horizontalSpacer_28 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_28)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_29 = QSpacerItem(85, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)

        self.pushButton_ImgExtract_preview = QPushButton(self.imageExtract_groupBox)
        self.pushButton_ImgExtract_preview.setObjectName(u"pushButton_ImgExtract_preview")
        sizePolicy2.setHeightForWidth(self.pushButton_ImgExtract_preview.sizePolicy().hasHeightForWidth())
        self.pushButton_ImgExtract_preview.setSizePolicy(sizePolicy2)

        self.horizontalLayout_22.addWidget(self.pushButton_ImgExtract_preview)

        self.pushButton_ImgExtract_save = QPushButton(self.imageExtract_groupBox)
        self.pushButton_ImgExtract_save.setObjectName(u"pushButton_ImgExtract_save")
        sizePolicy2.setHeightForWidth(self.pushButton_ImgExtract_save.sizePolicy().hasHeightForWidth())
        self.pushButton_ImgExtract_save.setSizePolicy(sizePolicy2)

        self.horizontalLayout_22.addWidget(self.pushButton_ImgExtract_save)

        self.pushButton_ImgExtract_erase = QPushButton(self.imageExtract_groupBox)
        self.pushButton_ImgExtract_erase.setObjectName(u"pushButton_ImgExtract_erase")
        sizePolicy2.setHeightForWidth(self.pushButton_ImgExtract_erase.sizePolicy().hasHeightForWidth())
        self.pushButton_ImgExtract_erase.setSizePolicy(sizePolicy2)

        self.horizontalLayout_22.addWidget(self.pushButton_ImgExtract_erase)


        self.verticalLayout_16.addLayout(self.horizontalLayout_22)

        self.groupBox_6 = QGroupBox(self.imageExtract_groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_xscale_10 = QLabel(self.groupBox_6)
        self.label_xscale_10.setObjectName(u"label_xscale_10")
        self.label_xscale_10.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_10.sizePolicy().hasHeightForWidth())
        self.label_xscale_10.setSizePolicy(sizePolicy3)
        self.label_xscale_10.setMinimumSize(QSize(150, 3))
        self.label_xscale_10.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_23.addWidget(self.label_xscale_10)

        self.horizontalSpacer_30 = QSpacerItem(54, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_30)

        self.spinBox_extract1_x_2 = QSpinBox(self.groupBox_6)
        self.spinBox_extract1_x_2.setObjectName(u"spinBox_extract1_x_2")
        self.spinBox_extract1_x_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_extract1_x_2.sizePolicy().hasHeightForWidth())
        self.spinBox_extract1_x_2.setSizePolicy(sizePolicy2)
        self.spinBox_extract1_x_2.setMinimumSize(QSize(50, 0))
        self.spinBox_extract1_x_2.setMinimum(0)
        self.spinBox_extract1_x_2.setMaximum(10000)
        self.spinBox_extract1_x_2.setValue(0)

        self.horizontalLayout_23.addWidget(self.spinBox_extract1_x_2)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy5)

        self.horizontalLayout_23.addWidget(self.label_18)

        self.spinBox_extract1_y_2 = QSpinBox(self.groupBox_6)
        self.spinBox_extract1_y_2.setObjectName(u"spinBox_extract1_y_2")
        self.spinBox_extract1_y_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_extract1_y_2.sizePolicy().hasHeightForWidth())
        self.spinBox_extract1_y_2.setSizePolicy(sizePolicy2)
        self.spinBox_extract1_y_2.setMinimumSize(QSize(50, 0))
        self.spinBox_extract1_y_2.setMinimum(0)
        self.spinBox_extract1_y_2.setMaximum(10000)
        self.spinBox_extract1_y_2.setValue(0)

        self.horizontalLayout_23.addWidget(self.spinBox_extract1_y_2)

        self.label_19 = QLabel(self.groupBox_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy5)

        self.horizontalLayout_23.addWidget(self.label_19)

        self.horizontalSpacer_31 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_31)


        self.verticalLayout_20.addLayout(self.horizontalLayout_23)


        self.verticalLayout_16.addWidget(self.groupBox_6)


        self.verticalLayout_4.addWidget(self.imageExtract_groupBox)

        self.rotate_groupBox = QGroupBox(self.stackedWidgetPage1)
        self.rotate_groupBox.setObjectName(u"rotate_groupBox")
        self.verticalLayout_18 = QVBoxLayout(self.rotate_groupBox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.radioButton_rotate0 = QRadioButton(self.rotate_groupBox)
        self.radioButton_rotate0.setObjectName(u"radioButton_rotate0")
        self.radioButton_rotate0.setChecked(True)

        self.verticalLayout_18.addWidget(self.radioButton_rotate0)

        self.radioButton_rotate90 = QRadioButton(self.rotate_groupBox)
        self.radioButton_rotate90.setObjectName(u"radioButton_rotate90")
        self.radioButton_rotate90.setChecked(False)

        self.verticalLayout_18.addWidget(self.radioButton_rotate90)

        self.radioButton_rotate180 = QRadioButton(self.rotate_groupBox)
        self.radioButton_rotate180.setObjectName(u"radioButton_rotate180")

        self.verticalLayout_18.addWidget(self.radioButton_rotate180)

        self.radioButton_rotate270 = QRadioButton(self.rotate_groupBox)
        self.radioButton_rotate270.setObjectName(u"radioButton_rotate270")

        self.verticalLayout_18.addWidget(self.radioButton_rotate270)

        self.checkBox_mirror = QCheckBox(self.rotate_groupBox)
        self.checkBox_mirror.setObjectName(u"checkBox_mirror")
        self.checkBox_mirror.setChecked(False)
        self.checkBox_mirror.setTristate(False)

        self.verticalLayout_18.addWidget(self.checkBox_mirror)


        self.verticalLayout_4.addWidget(self.rotate_groupBox)

        self.groupBox_rec = QGroupBox(self.stackedWidgetPage1)
        self.groupBox_rec.setObjectName(u"groupBox_rec")
        self.groupBox_rec.setEnabled(True)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_rec)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_xscale_2 = QLabel(self.groupBox_rec)
        self.label_xscale_2.setObjectName(u"label_xscale_2")
        self.label_xscale_2.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_2.sizePolicy().hasHeightForWidth())
        self.label_xscale_2.setSizePolicy(sizePolicy3)
        self.label_xscale_2.setMinimumSize(QSize(150, 3))
        self.label_xscale_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.label_xscale_2)

        self.horizontalSpacer_9 = QSpacerItem(54, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.spinBox_xorigin = QSpinBox(self.groupBox_rec)
        self.spinBox_xorigin.setObjectName(u"spinBox_xorigin")
        self.spinBox_xorigin.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_xorigin.sizePolicy().hasHeightForWidth())
        self.spinBox_xorigin.setSizePolicy(sizePolicy2)
        self.spinBox_xorigin.setMinimumSize(QSize(50, 0))
        self.spinBox_xorigin.setMinimum(0)
        self.spinBox_xorigin.setMaximum(10000)
        self.spinBox_xorigin.setValue(0)

        self.horizontalLayout_11.addWidget(self.spinBox_xorigin)

        self.label = QLabel(self.groupBox_rec)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.label)

        self.spinBox_yorigin = QSpinBox(self.groupBox_rec)
        self.spinBox_yorigin.setObjectName(u"spinBox_yorigin")
        self.spinBox_yorigin.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_yorigin.sizePolicy().hasHeightForWidth())
        self.spinBox_yorigin.setSizePolicy(sizePolicy2)
        self.spinBox_yorigin.setMinimumSize(QSize(50, 0))
        self.spinBox_yorigin.setMinimum(0)
        self.spinBox_yorigin.setMaximum(10000)
        self.spinBox_yorigin.setValue(0)

        self.horizontalLayout_11.addWidget(self.spinBox_yorigin)

        self.label_7 = QLabel(self.groupBox_rec)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.label_7)

        self.horizontalSpacer_10 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_xscale_7 = QLabel(self.groupBox_rec)
        self.label_xscale_7.setObjectName(u"label_xscale_7")
        self.label_xscale_7.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_7.sizePolicy().hasHeightForWidth())
        self.label_xscale_7.setSizePolicy(sizePolicy3)
        self.label_xscale_7.setMinimumSize(QSize(150, 3))
        self.label_xscale_7.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.label_xscale_7)

        self.horizontalSpacer_19 = QSpacerItem(54, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)

        self.spinBox_xwin = QSpinBox(self.groupBox_rec)
        self.spinBox_xwin.setObjectName(u"spinBox_xwin")
        self.spinBox_xwin.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_xwin.sizePolicy().hasHeightForWidth())
        self.spinBox_xwin.setSizePolicy(sizePolicy2)
        self.spinBox_xwin.setMinimumSize(QSize(50, 0))
        self.spinBox_xwin.setMinimum(0)
        self.spinBox_xwin.setMaximum(10000)
        self.spinBox_xwin.setValue(250)

        self.horizontalLayout_16.addWidget(self.spinBox_xwin)

        self.label_8 = QLabel(self.groupBox_rec)
        self.label_8.setObjectName(u"label_8")
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.label_8)

        self.spinBox_ywin = QSpinBox(self.groupBox_rec)
        self.spinBox_ywin.setObjectName(u"spinBox_ywin")
        self.spinBox_ywin.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_ywin.sizePolicy().hasHeightForWidth())
        self.spinBox_ywin.setSizePolicy(sizePolicy2)
        self.spinBox_ywin.setMinimumSize(QSize(50, 0))
        self.spinBox_ywin.setMinimum(0)
        self.spinBox_ywin.setMaximum(10000)
        self.spinBox_ywin.setValue(250)

        self.horizontalLayout_16.addWidget(self.spinBox_ywin)

        self.label_9 = QLabel(self.groupBox_rec)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.label_9)

        self.horizontalSpacer_20 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_20)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_xscale_4 = QLabel(self.groupBox_rec)
        self.label_xscale_4.setObjectName(u"label_xscale_4")
        self.label_xscale_4.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_4.sizePolicy().hasHeightForWidth())
        self.label_xscale_4.setSizePolicy(sizePolicy3)
        self.label_xscale_4.setMinimumSize(QSize(150, 3))
        self.label_xscale_4.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_13.addWidget(self.label_xscale_4)

        self.horizontalSpacer_13 = QSpacerItem(130, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.spinBox_overlapping = QSpinBox(self.groupBox_rec)
        self.spinBox_overlapping.setObjectName(u"spinBox_overlapping")
        self.spinBox_overlapping.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_overlapping.sizePolicy().hasHeightForWidth())
        self.spinBox_overlapping.setSizePolicy(sizePolicy2)
        self.spinBox_overlapping.setMinimumSize(QSize(50, 0))
        self.spinBox_overlapping.setMinimum(0)
        self.spinBox_overlapping.setMaximum(1000)
        self.spinBox_overlapping.setValue(50)

        self.horizontalLayout_13.addWidget(self.spinBox_overlapping)

        self.horizontalSpacer_14 = QSpacerItem(36, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_xscale_8 = QLabel(self.groupBox_rec)
        self.label_xscale_8.setObjectName(u"label_xscale_8")
        self.label_xscale_8.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_8.sizePolicy().hasHeightForWidth())
        self.label_xscale_8.setSizePolicy(sizePolicy3)
        self.label_xscale_8.setMinimumSize(QSize(150, 3))
        self.label_xscale_8.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_17.addWidget(self.label_xscale_8)

        self.horizontalSpacer_21 = QSpacerItem(59, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_21)

        self.spinBox_xNBoxes = QSpinBox(self.groupBox_rec)
        self.spinBox_xNBoxes.setObjectName(u"spinBox_xNBoxes")
        self.spinBox_xNBoxes.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_xNBoxes.sizePolicy().hasHeightForWidth())
        self.spinBox_xNBoxes.setSizePolicy(sizePolicy2)
        self.spinBox_xNBoxes.setMinimumSize(QSize(50, 0))
        self.spinBox_xNBoxes.setMinimum(0)
        self.spinBox_xNBoxes.setMaximum(100)
        self.spinBox_xNBoxes.setValue(1)

        self.horizontalLayout_17.addWidget(self.spinBox_xNBoxes)

        self.label_10 = QLabel(self.groupBox_rec)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)

        self.horizontalLayout_17.addWidget(self.label_10)

        self.spinBox_yNBoxes = QSpinBox(self.groupBox_rec)
        self.spinBox_yNBoxes.setObjectName(u"spinBox_yNBoxes")
        self.spinBox_yNBoxes.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.spinBox_yNBoxes.sizePolicy().hasHeightForWidth())
        self.spinBox_yNBoxes.setSizePolicy(sizePolicy2)
        self.spinBox_yNBoxes.setMinimumSize(QSize(50, 0))
        self.spinBox_yNBoxes.setMinimum(0)
        self.spinBox_yNBoxes.setMaximum(100)
        self.spinBox_yNBoxes.setValue(1)

        self.horizontalLayout_17.addWidget(self.spinBox_yNBoxes)

        self.label_11 = QLabel(self.groupBox_rec)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)

        self.horizontalLayout_17.addWidget(self.label_11)

        self.horizontalSpacer_22 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_8 = QSpacerItem(183, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.pushButton_draw = QPushButton(self.groupBox_rec)
        self.pushButton_draw.setObjectName(u"pushButton_draw")
        sizePolicy2.setHeightForWidth(self.pushButton_draw.sizePolicy().hasHeightForWidth())
        self.pushButton_draw.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.pushButton_draw)

        self.pushButton_erase = QPushButton(self.groupBox_rec)
        self.pushButton_erase.setObjectName(u"pushButton_erase")
        sizePolicy2.setHeightForWidth(self.pushButton_erase.sizePolicy().hasHeightForWidth())
        self.pushButton_erase.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.pushButton_erase)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.verticalLayout_4.addWidget(self.groupBox_rec)

        self.verticalSpacer = QSpacerItem(20, 204, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_11 = QSpacerItem(280, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.pushButton_next1 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_next1.setObjectName(u"pushButton_next1")
        self.pushButton_next1.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pushButton_next1.sizePolicy().hasHeightForWidth())
        self.pushButton_next1.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.pushButton_next1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.verticalLayout_8 = QVBoxLayout(self.stackedWidgetPage2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.model_groupBox = QGroupBox(self.stackedWidgetPage2)
        self.model_groupBox.setObjectName(u"model_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.model_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.model_groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(432, 93))
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.model_groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setMinimumSize(QSize(150, 3))
        self.label_5.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_modelpath = QLineEdit(self.model_groupBox)
        self.lineEdit_modelpath.setObjectName(u"lineEdit_modelpath")
        sizePolicy4.setHeightForWidth(self.lineEdit_modelpath.sizePolicy().hasHeightForWidth())
        self.lineEdit_modelpath.setSizePolicy(sizePolicy4)
        self.lineEdit_modelpath.setMinimumSize(QSize(200, 0))
        self.lineEdit_modelpath.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_modelpath)

        self.toolButton_modelpath = QToolButton(self.model_groupBox)
        self.toolButton_modelpath.setObjectName(u"toolButton_modelpath")

        self.horizontalLayout_6.addWidget(self.toolButton_modelpath)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(229, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.pushButton_loadmodel = QPushButton(self.model_groupBox)
        self.pushButton_loadmodel.setObjectName(u"pushButton_loadmodel")
        self.pushButton_loadmodel.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pushButton_loadmodel.sizePolicy().hasHeightForWidth())
        self.pushButton_loadmodel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.pushButton_loadmodel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addWidget(self.model_groupBox)

        self.minorSegmentation_groupBox = QGroupBox(self.stackedWidgetPage2)
        self.minorSegmentation_groupBox.setObjectName(u"minorSegmentation_groupBox")
        self.verticalLayout_23 = QVBoxLayout(self.minorSegmentation_groupBox)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_24 = QLabel(self.minorSegmentation_groupBox)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMinimumSize(QSize(0, 0))
        self.label_24.setMaximumSize(QSize(432, 93))
        self.label_24.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_24.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_24)

        self.checkBox_enableMinorSegm = QCheckBox(self.minorSegmentation_groupBox)
        self.checkBox_enableMinorSegm.setObjectName(u"checkBox_enableMinorSegm")
        self.checkBox_enableMinorSegm.setChecked(False)
        self.checkBox_enableMinorSegm.setTristate(False)

        self.verticalLayout_23.addWidget(self.checkBox_enableMinorSegm)


        self.verticalLayout_8.addWidget(self.minorSegmentation_groupBox)

        self.prcss_groupBox = QGroupBox(self.stackedWidgetPage2)
        self.prcss_groupBox.setObjectName(u"prcss_groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.prcss_groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.progressBar = QProgressBar(self.prcss_groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_4.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_12 = QSpacerItem(229, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.pushButton_process = QPushButton(self.prcss_groupBox)
        self.pushButton_process.setObjectName(u"pushButton_process")
        sizePolicy2.setHeightForWidth(self.pushButton_process.sizePolicy().hasHeightForWidth())
        self.pushButton_process.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.pushButton_process)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addWidget(self.prcss_groupBox)

        self.scale_groupBox = QGroupBox(self.stackedWidgetPage2)
        self.scale_groupBox.setObjectName(u"scale_groupBox")
        self.verticalLayout_9 = QVBoxLayout(self.scale_groupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.scale_groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(432, 93))
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_6.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_xscale_5 = QLabel(self.scale_groupBox)
        self.label_xscale_5.setObjectName(u"label_xscale_5")
        self.label_xscale_5.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_5.sizePolicy().hasHeightForWidth())
        self.label_xscale_5.setSizePolicy(sizePolicy3)
        self.label_xscale_5.setMinimumSize(QSize(150, 3))
        self.label_xscale_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_15.addWidget(self.label_xscale_5)

        self.horizontalSpacer_16 = QSpacerItem(54, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.doubleSpinBox_xscale = QDoubleSpinBox(self.scale_groupBox)
        self.doubleSpinBox_xscale.setObjectName(u"doubleSpinBox_xscale")
        self.doubleSpinBox_xscale.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_xscale.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_xscale.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_xscale.setMinimumSize(QSize(50, 0))
        self.doubleSpinBox_xscale.setValue(1.000000000000000)

        self.horizontalLayout_15.addWidget(self.doubleSpinBox_xscale)

        self.label_15 = QLabel(self.scale_groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)

        self.horizontalLayout_15.addWidget(self.label_15)

        self.horizontalSpacer_17 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_xscale_6 = QLabel(self.scale_groupBox)
        self.label_xscale_6.setObjectName(u"label_xscale_6")
        self.label_xscale_6.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_xscale_6.sizePolicy().hasHeightForWidth())
        self.label_xscale_6.setSizePolicy(sizePolicy3)
        self.label_xscale_6.setMinimumSize(QSize(150, 3))
        self.label_xscale_6.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.label_xscale_6)

        self.horizontalSpacer_18 = QSpacerItem(54, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)

        self.doubleSpinBox_yscale = QDoubleSpinBox(self.scale_groupBox)
        self.doubleSpinBox_yscale.setObjectName(u"doubleSpinBox_yscale")
        self.doubleSpinBox_yscale.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_yscale.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_yscale.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_yscale.setMinimumSize(QSize(50, 0))
        self.doubleSpinBox_yscale.setValue(1.000000000000000)

        self.horizontalLayout_18.addWidget(self.doubleSpinBox_yscale)

        self.label_16 = QLabel(self.scale_groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)

        self.horizontalLayout_18.addWidget(self.label_16)

        self.horizontalSpacer_23 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_23)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_15 = QSpacerItem(229, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.pushButton_scale = QPushButton(self.scale_groupBox)
        self.pushButton_scale.setObjectName(u"pushButton_scale")
        sizePolicy2.setHeightForWidth(self.pushButton_scale.sizePolicy().hasHeightForWidth())
        self.pushButton_scale.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.pushButton_scale)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)


        self.verticalLayout_8.addWidget(self.scale_groupBox)

        self.SPD_groupBox = QGroupBox(self.stackedWidgetPage2)
        self.SPD_groupBox.setObjectName(u"SPD_groupBox")
        self.verticalLayout_11 = QVBoxLayout(self.SPD_groupBox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.radioButton_rr = QRadioButton(self.SPD_groupBox)
        self.radioButton_rr.setObjectName(u"radioButton_rr")
        self.radioButton_rr.setChecked(True)

        self.verticalLayout_15.addWidget(self.radioButton_rr)

        self.radioButton_gs = QRadioButton(self.SPD_groupBox)
        self.radioButton_gs.setObjectName(u"radioButton_gs")

        self.verticalLayout_15.addWidget(self.radioButton_gs)

        self.radioButton_sw = QRadioButton(self.SPD_groupBox)
        self.radioButton_sw.setObjectName(u"radioButton_sw")

        self.verticalLayout_15.addWidget(self.radioButton_sw)


        self.verticalLayout_11.addLayout(self.verticalLayout_15)


        self.verticalLayout_8.addWidget(self.SPD_groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 676, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_prev = QPushButton(self.stackedWidgetPage2)
        self.pushButton_prev.setObjectName(u"pushButton_prev")
        sizePolicy2.setHeightForWidth(self.pushButton_prev.sizePolicy().hasHeightForWidth())
        self.pushButton_prev.setSizePolicy(sizePolicy2)

        self.horizontalLayout_19.addWidget(self.pushButton_prev)

        self.horizontalSpacer_24 = QSpacerItem(169, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_24)

        self.pushButton_next2 = QPushButton(self.stackedWidgetPage2)
        self.pushButton_next2.setObjectName(u"pushButton_next2")
        sizePolicy2.setHeightForWidth(self.pushButton_next2.sizePolicy().hasHeightForWidth())
        self.pushButton_next2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_19.addWidget(self.pushButton_next2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(229, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        sizePolicy2.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pushButton_save)

        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        sizePolicy2.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        ProcessConf.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProcessConf)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1147, 21))
        ProcessConf.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProcessConf)
        self.statusbar.setObjectName(u"statusbar")
        ProcessConf.setStatusBar(self.statusbar)

        self.retranslateUi(ProcessConf)

        self.tab5.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ProcessConf)
    # setupUi

    def retranslateUi(self, ProcessConf):
        ProcessConf.setWindowTitle(QCoreApplication.translate("ProcessConf", u"Process Configuration", None))
        self.tab5.setTabText(self.tab5.indexOf(self.tab_6), QCoreApplication.translate("ProcessConf", u"Tab 0", None))
        self.tab5.setTabText(self.tab5.indexOf(self.tab), QCoreApplication.translate("ProcessConf", u"Tab 1", None))
        self.tab5.setTabText(self.tab5.indexOf(self.tab_2), QCoreApplication.translate("ProcessConf", u"Tab 2", None))
        self.tab5.setTabText(self.tab5.indexOf(self.tab_3), QCoreApplication.translate("ProcessConf", u"Tab 3", None))
        self.tab5.setTabText(self.tab5.indexOf(self.tab_5), QCoreApplication.translate("ProcessConf", u"Tab 4", None))
        self.tab5.setTabText(self.tab5.indexOf(self.tab_4), QCoreApplication.translate("ProcessConf", u"Tab 5", None))
        self.image_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Golden Template", None))
        self.label_3.setText(QCoreApplication.translate("ProcessConf", u"<html><head/><body><p align=\"justify\">Insertar Imagen que se utilizara como referencia para configuracion de las siguientes caracteristicas: modelo de detector simantico de granulometria grande y funcion de ajuste de granulometria</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ProcessConf", u"Input Image", None))
        self.toolButton_imgpath.setText(QCoreApplication.translate("ProcessConf", u"...", None))
        self.Lookuptable_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Lookup Table", None))
        self.label_20.setText(QCoreApplication.translate("ProcessConf", u"<html><head/><body><p align=\"justify\">Insertar Archivo de texto con el arreglo de la table Lookup para equalizar la imagen.</p></body></html>", None))
        self.checkBox_lookuptable.setText(QCoreApplication.translate("ProcessConf", u"Enable Lookup Table", None))
        self.label_21.setText(QCoreApplication.translate("ProcessConf", u"Lookup table file", None))
        self.toolButton_lookuppath.setText(QCoreApplication.translate("ProcessConf", u"...", None))
        self.imageExtract_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Image Extract", None))
        self.label_xscale_3.setText(QCoreApplication.translate("ProcessConf", u"Point1", None))
        self.label_12.setText(QCoreApplication.translate("ProcessConf", u"X", None))
        self.label_13.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.label_xscale_9.setText(QCoreApplication.translate("ProcessConf", u"Point2", None))
        self.label_14.setText(QCoreApplication.translate("ProcessConf", u"X", None))
        self.label_17.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.pushButton_ImgExtract_preview.setText(QCoreApplication.translate("ProcessConf", u"Preview", None))
        self.pushButton_ImgExtract_save.setText(QCoreApplication.translate("ProcessConf", u"Extract", None))
        self.pushButton_ImgExtract_erase.setText(QCoreApplication.translate("ProcessConf", u"Erase", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ProcessConf", u"Scale", None))
        self.label_xscale_10.setText(QCoreApplication.translate("ProcessConf", u"Scale", None))
        self.label_18.setText(QCoreApplication.translate("ProcessConf", u"X", None))
        self.label_19.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.rotate_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Rotate", None))
        self.radioButton_rotate0.setText(QCoreApplication.translate("ProcessConf", u"None", None))
        self.radioButton_rotate90.setText(QCoreApplication.translate("ProcessConf", u"90", None))
        self.radioButton_rotate180.setText(QCoreApplication.translate("ProcessConf", u"180", None))
        self.radioButton_rotate270.setText(QCoreApplication.translate("ProcessConf", u"270", None))
        self.checkBox_mirror.setText(QCoreApplication.translate("ProcessConf", u"Mirror", None))
        self.groupBox_rec.setTitle(QCoreApplication.translate("ProcessConf", u"Windowing", None))
        self.label_xscale_2.setText(QCoreApplication.translate("ProcessConf", u"Origins", None))
        self.label.setText(QCoreApplication.translate("ProcessConf", u"X", None))
        self.label_7.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.label_xscale_7.setText(QCoreApplication.translate("ProcessConf", u"Windowing", None))
        self.label_8.setText(QCoreApplication.translate("ProcessConf", u"X", None))
        self.label_9.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.label_xscale_4.setText(QCoreApplication.translate("ProcessConf", u"Windowing Overlapping", None))
        self.label_xscale_8.setText(QCoreApplication.translate("ProcessConf", u"Number Boxes", None))
        self.label_10.setText(QCoreApplication.translate("ProcessConf", u"X", None))
        self.label_11.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.pushButton_draw.setText(QCoreApplication.translate("ProcessConf", u"Draw", None))
        self.pushButton_erase.setText(QCoreApplication.translate("ProcessConf", u"Erase", None))
        self.pushButton_next1.setText(QCoreApplication.translate("ProcessConf", u"Next", None))
        self.model_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Model", None))
        self.label_4.setText(QCoreApplication.translate("ProcessConf", u"<html><head/><body><p>Modelo preentrenado de Segmentacion de Instanciasl con extension .torch, el cual separa granulometria de cierto tama\u00f1o para su posterior analisis de segmentaci\u00f3n.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("ProcessConf", u"Model File", None))
        self.toolButton_modelpath.setText(QCoreApplication.translate("ProcessConf", u"...", None))
        self.pushButton_loadmodel.setText(QCoreApplication.translate("ProcessConf", u"Load", None))
        self.minorSegmentation_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Medir Segmentaci\u00f3n Menor", None))
        self.label_24.setText(QCoreApplication.translate("ProcessConf", u"<html><head/><body><p>Al activarse esta opci\u00f3n el sistema mide la granulometr\u00eda del \u00e1rea de no detecci\u00f3n.</p></body></html>", None))
        self.checkBox_enableMinorSegm.setText(QCoreApplication.translate("ProcessConf", u"Enable Minor Segmentation", None))
        self.prcss_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Image Process", None))
        self.pushButton_process.setText(QCoreApplication.translate("ProcessConf", u"Process", None))
        self.scale_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Scale", None))
        self.label_6.setText(QCoreApplication.translate("ProcessConf", u"<html><head/><body><p>Escala Pixel -&gt; Real en mm</p></body></html>", None))
        self.label_xscale_5.setText(QCoreApplication.translate("ProcessConf", u"Scale X", None))
        self.label_15.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.label_xscale_6.setText(QCoreApplication.translate("ProcessConf", u"Scale Y", None))
        self.label_16.setText(QCoreApplication.translate("ProcessConf", u"Y", None))
        self.pushButton_scale.setText(QCoreApplication.translate("ProcessConf", u"Scale", None))
        self.SPD_groupBox.setTitle(QCoreApplication.translate("ProcessConf", u"Size Particle Distribution", None))
        self.radioButton_rr.setText(QCoreApplication.translate("ProcessConf", u"Rosin-Rambler", None))
        self.radioButton_gs.setText(QCoreApplication.translate("ProcessConf", u"Gaudin-Shuhmman", None))
        self.radioButton_sw.setText(QCoreApplication.translate("ProcessConf", u"Swebrec", None))
        self.pushButton_prev.setText(QCoreApplication.translate("ProcessConf", u"Previous", None))
        self.pushButton_next2.setText(QCoreApplication.translate("ProcessConf", u"Next", None))
        self.pushButton_save.setText(QCoreApplication.translate("ProcessConf", u"Accept", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("ProcessConf", u"Cancel", None))
    # retranslateUi

