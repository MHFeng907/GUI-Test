# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    clickButton(waitForObject(names.mainWidget_rhombus_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 120, 54, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 92, 49, 32, 252, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 695, 394, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 619, 84, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 643, 459, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton_2))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 181, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 74, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton_2))
    test.vp("VP1_origin")
    
    activateItem(waitForObjectItem(names.mainWidget_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.mainWidget_File_QMenu, "Save"))
    type(waitForObject(names.fileNameEdit_QLineEdit), "test")
    type(waitForObject(names.fileNameEdit_QLineEdit), "dat")
    test.vp("VP1_before_save_dialog")
    clickButton(waitForObject(names.qFileDialog_Save_QPushButton))
    sendEvent("QCloseEvent", waitForObject(names.mainWidget_MainWidget))

    startApplication("FlowelementChart")
    activateItem(waitForObjectItem(names.mainWidget_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.mainWidget_File_QMenu, "Open"))
    test.vp("VP1_after_save_dialog")
    type(waitForObject(names.fileNameEdit_QLineEdit), "testdat")
    mouseClick(waitForImage("image_openfile"))
    test.vp("VP1_open_pic")