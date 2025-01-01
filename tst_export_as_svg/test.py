# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    clickButton(waitForObject(names.mainWidget_rhombus_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 71, 48, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 101, 50, 49, 249, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 308, 273, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 132, 99, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 99, -1, Qt.NoModifier, Qt.LeftButton)
    
    activateItem(waitForObjectItem(names.mainWidget_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.mainWidget_File_QMenu, "Export"))
    mouseClick(waitForObject(names.fileNameEdit_QLineEdit), 33, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.fileNameEdit_QLineEdit), "svgtest")
    test.vp("VP1_before_svg")
    clickButton(waitForObject(names.qFileDialog_Save_QPushButton))
    activateItem(waitForObjectItem(names.mainWidget_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.mainWidget_File_QMenu, "Export"))
    test.vp("VP1_after_svg")
