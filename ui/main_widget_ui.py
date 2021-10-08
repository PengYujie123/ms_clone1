# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menu_Options = QtWidgets.QMenu(self.menubar)
        self.menu_Options.setObjectName("menu_Options")
        self.menu_Window = QtWidgets.QMenu(self.menubar)
        self.menu_Window.setObjectName("menu_Window")
        self.edit = QtWidgets.QMenu(self.menubar)
        self.edit.setObjectName("edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 40))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen_seismograms = QtWidgets.QAction(MainWindow)
        self.actionopen_seismograms.setObjectName("actionopen_seismograms")
        self.actionlast_seismograms = QtWidgets.QAction(MainWindow)
        self.actionlast_seismograms.setObjectName("actionlast_seismograms")
        self.actionnext_seismograms = QtWidgets.QAction(MainWindow)
        self.actionnext_seismograms.setObjectName("actionnext_seismograms")
        self.actionopen_mining_map = QtWidgets.QAction(MainWindow)
        self.actionopen_mining_map.setObjectName("actionopen_mining_map")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionreset = QtWidgets.QAction(MainWindow)
        self.actionreset.setObjectName("actionreset")
        self.actionside_by_side = QtWidgets.QAction(MainWindow)
        self.actionside_by_side.setObjectName("actionside_by_side")
        self.actionstack = QtWidgets.QAction(MainWindow)
        self.actionstack.setObjectName("actionstack")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionPp = QtWidgets.QAction(MainWindow)
        self.actionPp.setObjectName("actionPp")
        self.actionPk = QtWidgets.QAction(MainWindow)
        self.actionPk.setObjectName("actionPk")
        self.actionSp = QtWidgets.QAction(MainWindow)
        self.actionSp.setObjectName("actionSp")
        self.actionSk = QtWidgets.QAction(MainWindow)
        self.actionSk.setObjectName("actionSk")
        self.actioncancel = QtWidgets.QAction(MainWindow)
        self.actioncancel.setObjectName("actioncancel")
        self.actionZn = QtWidgets.QAction(MainWindow)
        self.actionZn.setObjectName("actionZn")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSY = QtWidgets.QAction(MainWindow)
        self.actionSY.setObjectName("actionSY")
        self.actionSY_2 = QtWidgets.QAction(MainWindow)
        self.actionSY_2.setObjectName("actionSY_2")
        self.actionASY = QtWidgets.QAction(MainWindow)
        self.actionASY.setObjectName("actionASY")
        self.actionX = QtWidgets.QAction(MainWindow)
        self.actionX.setObjectName("actionX")
        self.actionX_2 = QtWidgets.QAction(MainWindow)
        self.actionX_2.setObjectName("actionX_2")
        self.actionY = QtWidgets.QAction(MainWindow)
        self.actionY.setObjectName("actionY")
        self.actionY_2 = QtWidgets.QAction(MainWindow)
        self.actionY_2.setObjectName("actionY_2")
        self.actionSP = QtWidgets.QAction(MainWindow)
        self.actionSP.setObjectName("actionSP")
        self.actionKX = QtWidgets.QAction(MainWindow)
        self.actionKX.setObjectName("actionKX")
        self.actionKY = QtWidgets.QAction(MainWindow)
        self.actionKY.setObjectName("actionKY")
        self.actionKYY = QtWidgets.QAction(MainWindow)
        self.actionKYY.setObjectName("actionKYY")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionPwave_filt = QtWidgets.QAction(MainWindow)
        self.actionPwave_filt.setObjectName("actionPwave_filt")
        self.actionPwave_cut = QtWidgets.QAction(MainWindow)
        self.actionPwave_cut.setObjectName("actionPwave_cut")
        self.actionSwave_filt = QtWidgets.QAction(MainWindow)
        self.actionSwave_filt.setObjectName("actionSwave_filt")
        self.actionSwave_cut = QtWidgets.QAction(MainWindow)
        self.actionSwave_cut.setObjectName("actionSwave_cut")
        self.actionShow_Hide = QtWidgets.QAction(MainWindow)
        self.actionShow_Hide.setObjectName("actionShow_Hide")
        self.actionCancel = QtWidgets.QAction(MainWindow)
        self.actionCancel.setObjectName("actionCancel")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDelete_2 = QtWidgets.QAction(MainWindow)
        self.actionDelete_2.setObjectName("actionDelete_2")
        self.actionprint = QtWidgets.QAction(MainWindow)
        self.actionprint.setObjectName("actionprint")
        self.actionauto_sign_wave = QtWidgets.QAction(MainWindow)
        self.actionauto_sign_wave.setObjectName("actionauto_sign_wave")
        self.actionwaveform_chara = QtWidgets.QAction(MainWindow)
        self.actionwaveform_chara.setObjectName("actionwaveform_chara")
        self.actionwaveform_zoom = QtWidgets.QAction(MainWindow)
        self.actionwaveform_zoom.setObjectName("actionwaveform_zoom")
        self.actionwindow_switch = QtWidgets.QAction(MainWindow)
        self.actionwindow_switch.setObjectName("actionwindow_switch")
        self.actionsign_wave_tool = QtWidgets.QAction(MainWindow)
        self.actionsign_wave_tool.setObjectName("actionsign_wave_tool")
        self.actionlocate_tool = QtWidgets.QAction(MainWindow)
        self.actionlocate_tool.setObjectName("actionlocate_tool")
        self.actionpara = QtWidgets.QAction(MainWindow)
        self.actionpara.setObjectName("actionpara")
        self.actionlocate_way = QtWidgets.QAction(MainWindow)
        self.actionlocate_way.setObjectName("actionlocate_way")
        self.actionmin_algorithm = QtWidgets.QAction(MainWindow)
        self.actionmin_algorithm.setObjectName("actionmin_algorithm")
        self.actioninit_para = QtWidgets.QAction(MainWindow)
        self.actioninit_para.setObjectName("actioninit_para")
        self.actiondimension_set = QtWidgets.QAction(MainWindow)
        self.actiondimension_set.setObjectName("actiondimension_set")
        self.actionpara_set = QtWidgets.QAction(MainWindow)
        self.actionpara_set.setObjectName("actionpara_set")
        self.actionshow_set = QtWidgets.QAction(MainWindow)
        self.actionshow_set.setObjectName("actionshow_set")
        self.actionsign_result = QtWidgets.QAction(MainWindow)
        self.actionsign_result.setObjectName("actionsign_result")
        self.actioncalculate = QtWidgets.QAction(MainWindow)
        self.actioncalculate.setObjectName("actioncalculate")
        self.actionamplitude_calculate = QtWidgets.QAction(MainWindow)
        self.actionamplitude_calculate.setObjectName("actionamplitude_calculate")
        self.actionintegral_calculate = QtWidgets.QAction(MainWindow)
        self.actionintegral_calculate.setObjectName("actionintegral_calculate")
        self.actionundo = QtWidgets.QAction(MainWindow)
        self.actionundo.setObjectName("actionundo")
        self.actionredo = QtWidgets.QAction(MainWindow)
        self.actionredo.setObjectName("actionredo")
        self.actiontime = QtWidgets.QAction(MainWindow)
        self.actiontime.setObjectName("actiontime")
        self.actionfolder = QtWidgets.QAction(MainWindow)
        self.actionfolder.setObjectName("actionfolder")
        self.actioncad = QtWidgets.QAction(MainWindow)
        self.actioncad.setObjectName("actioncad")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menu_File.addAction(self.actionopen_seismograms)
        self.menu_File.addAction(self.actionopen_mining_map)
        self.menu_File.addAction(self.actionprint)
        self.menu_File.addAction(self.actionclose)
        self.menu_File.addAction(self.actionexit)
        self.menuHelp.addAction(self.actionabout)
        self.menuHelp.addAction(self.actionhelp)
        self.menu_Options.addAction(self.actiontime)
        self.menu_Options.addAction(self.actionpara)
        self.menu_Options.addAction(self.actionlocate_way)
        self.menu_Options.addAction(self.action_3)
        self.menu_Options.addAction(self.actionfolder)
        self.menu_Options.addAction(self.actioncad)
        self.menu_Window.addAction(self.actionlast_seismograms)
        self.menu_Window.addAction(self.actionnext_seismograms)
        self.menu_Window.addAction(self.actionReset)
        self.menu_Window.addAction(self.actionside_by_side)
        self.edit.addAction(self.actionundo)
        self.edit.addAction(self.actionredo)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.edit.menuAction())
        self.menubar.addAction(self.menu_Options.menuAction())
        self.menubar.addAction(self.menu_Window.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actiontime)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionopen_seismograms)
        self.toolBar.addAction(self.actionlast_seismograms)
        self.toolBar.addAction(self.actionnext_seismograms)
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_File.setTitle(_translate("MainWindow", "文件 File(F)"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.menu_Options.setTitle(_translate("MainWindow", "设置"))
        self.menu_Window.setTitle(_translate("MainWindow", "窗口 "))
        self.edit.setTitle(_translate("MainWindow", "编辑"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionopen_seismograms.setText(_translate("MainWindow", "打开微震文件"))
        self.actionopen_seismograms.setToolTip(_translate("MainWindow", "打开解析W震动文件，并以波形显示"))
        self.actionlast_seismograms.setText(_translate("MainWindow", "上一个"))
        self.actionlast_seismograms.setToolTip(_translate("MainWindow", "W震动文件的切换，切换至上一文件"))
        self.actionnext_seismograms.setText(_translate("MainWindow", "下一个"))
        self.actionnext_seismograms.setToolTip(_translate("MainWindow", "W震动文件的切换，切换至下一文件"))
        self.actionopen_mining_map.setText(_translate("MainWindow", "打开矿图文件"))
        self.actionopen_mining_map.setToolTip(_translate("MainWindow", "打开CAD文件"))
        self.actionclose.setText(_translate("MainWindow", "关闭"))
        self.actionclose.setToolTip(_translate("MainWindow", "关闭所有图形显示区所有窗口"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.actionexit.setToolTip(_translate("MainWindow", "退出本软件"))
        self.actionreset.setText(_translate("MainWindow", "reset"))
        self.actionside_by_side.setText(_translate("MainWindow", "隐藏标波窗口"))
        self.actionstack.setText(_translate("MainWindow", "层叠显示窗口"))
        self.actionMinimize.setText(_translate("MainWindow", "窗口最小化"))
        self.actionReset.setText(_translate("MainWindow", "显示标波窗口"))
        self.actionsave.setText(_translate("MainWindow", "Save"))
        self.actionPp.setText(_translate("MainWindow", "Pp"))
        self.actionPk.setText(_translate("MainWindow", "Pk"))
        self.actionSp.setText(_translate("MainWindow", "Sp"))
        self.actionSk.setText(_translate("MainWindow", "Sk"))
        self.actioncancel.setText(_translate("MainWindow", "Cancel"))
        self.actionZn.setText(_translate("MainWindow", "Zn"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionSY.setText(_translate("MainWindow", "SY+"))
        self.actionSY_2.setText(_translate("MainWindow", "SY-"))
        self.actionASY.setText(_translate("MainWindow", "ASY"))
        self.actionX.setText(_translate("MainWindow", "X+"))
        self.actionX_2.setText(_translate("MainWindow", "X-"))
        self.actionY.setText(_translate("MainWindow", "Y+"))
        self.actionY_2.setText(_translate("MainWindow", "Y-"))
        self.actionSP.setText(_translate("MainWindow", "SP"))
        self.actionKX.setText(_translate("MainWindow", "KX"))
        self.actionKY.setText(_translate("MainWindow", "KY"))
        self.actionKYY.setText(_translate("MainWindow", "KYY"))
        self.action.setText(_translate("MainWindow", "+"))
        self.action_2.setText(_translate("MainWindow", "-"))
        self.actionPwave_filt.setText(_translate("MainWindow", "P波标记筛选"))
        self.actionPwave_cut.setText(_translate("MainWindow", "P波标记截取"))
        self.actionSwave_filt.setText(_translate("MainWindow", "S波标记筛选"))
        self.actionSwave_cut.setText(_translate("MainWindow", "S波标记截取"))
        self.actionShow_Hide.setText(_translate("MainWindow", "Show/Hide"))
        self.actionCancel.setText(_translate("MainWindow", "Cancel"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionDelete_2.setText(_translate("MainWindow", "Delete"))
        self.actionprint.setText(_translate("MainWindow", "打印"))
        self.actionprint.setToolTip(_translate("MainWindow", "打印当前页面"))
        self.actionauto_sign_wave.setText(_translate("MainWindow", "自动标波"))
        self.actionwaveform_chara.setText(_translate("MainWindow", "波形属性"))
        self.actionwaveform_zoom.setText(_translate("MainWindow", "波形缩放工具箱"))
        self.actionwindow_switch.setText(_translate("MainWindow", "窗口切换工具箱"))
        self.actionsign_wave_tool.setText(_translate("MainWindow", "标波工具箱"))
        self.actionlocate_tool.setText(_translate("MainWindow", "定位工具箱"))
        self.actionpara.setText(_translate("MainWindow", "传感器"))
        self.actionlocate_way.setText(_translate("MainWindow", "定位算法"))
        self.actionmin_algorithm.setText(_translate("MainWindow", "最小算法"))
        self.actioninit_para.setText(_translate("MainWindow", "初始参数"))
        self.actiondimension_set.setText(_translate("MainWindow", "维数设置"))
        self.actionpara_set.setText(_translate("MainWindow", "参数设置"))
        self.actionshow_set.setText(_translate("MainWindow", "显示设置"))
        self.actionsign_result.setText(_translate("MainWindow", "波形标记结果"))
        self.actioncalculate.setText(_translate("MainWindow", "手动计算"))
        self.actionamplitude_calculate.setText(_translate("MainWindow", "自动以振幅计算"))
        self.actionintegral_calculate.setText(_translate("MainWindow", "自动以积分计算"))
        self.actionundo.setText(_translate("MainWindow", "撤销"))
        self.actionredo.setText(_translate("MainWindow", "恢复"))
        self.actiontime.setText(_translate("MainWindow", "时间"))
        self.actionfolder.setText(_translate("MainWindow", "微震波形文件夹"))
        self.actioncad.setText(_translate("MainWindow", "CAD文件路径"))
        self.action_3.setText(_translate("MainWindow", "微震事件显示"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionhelp.setText(_translate("MainWindow", "使用帮助"))
