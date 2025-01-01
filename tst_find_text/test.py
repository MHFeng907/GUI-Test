# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    doubleClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 291, 144, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 521, 156, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP1_before")
    mouseClick(waitForObject(names.mainWidget_searchBox_QLineEdit), 333, 17, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "<CapsLock>")
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "T")
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "<CapsLock>")
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "ext")
    clickButton(waitForObject(names.mainWidget_searchButton_QPushButton))
    test.vp("VP1_dialog")
    mouseClick(waitForObject(names.o_QLineEdit_2), 113, 12, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.o_QLineEdit_2), "<CapsLock>")
    type(waitForObject(names.o_QLineEdit_2), "C")
    type(waitForObject(names.o_QLineEdit_2), "<CapsLock>")
    type(waitForObject(names.o_QLineEdit_2), "hange")
    clickButton(waitForObject(names.o_OK_QPushButton_2))
    test.vp("VP1_after")
