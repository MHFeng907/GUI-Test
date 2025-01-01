# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    test.vp("VP1")
    clickButton(waitForObject(names.mainWidget_rhombus_button_QPushButton))
    test.vp("VP2")
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 91, 45, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 94, 44, 50, 220, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 709, 270, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP3")
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 132, 101, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 300, 321, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP4")
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 166, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 193, 52, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP5")
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 111, 50, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_color_button_QPushButton))
    mouseClick(waitForObject(names.basic_colors_QtPrivate_QWellArray), 149, 60, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.select_Color_OK_QPushButton))
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 690, 336, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP6")
    
    # 撤销
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    test.vp("VP5")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    test.vp("VP4")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    test.vp("VP3")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    test.vp("VP2")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    test.vp("VP1")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    test.vp("VP0")
    
    # 重做
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Y>")
    test.vp("VP1")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Y>")
    test.vp("VP2")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Y>")
    test.vp("VP3")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Y>")
    test.vp("VP4")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Y>")
    test.vp("VP5")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Y>")
    test.vp("VP6")
    