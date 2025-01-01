# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    doubleClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 334, 162, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 449, 111, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_searchBox_QLineEdit), 303, 25, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "<CapsLock>")
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "T")
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "<CapsLock>")
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "ext")
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 535, 160, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_searchBox_QLineEdit), 338, 18, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWidget_searchBox_QLineEdit), "<Ctrl+F>")
    test.vp("VP1_after_f")