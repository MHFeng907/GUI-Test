# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    clickButton(waitForObject(names.mainWidget_rhombus_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 92, 66, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 107, 50, 39, 290, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 381, 313, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.o_QInputDialog), 290, 204, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 100, 0, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    test.vp("VP1_before")
    mouseDrag(waitForObject(names.o_QInputDialog), 104, 71, 416, 452, 1, Qt.LeftButton)
    test.vp("VP1_select")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+C>")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+V>")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    mouseDrag(waitForObject(names.o_QInputDialog), 126, 61, 356, 399, 1, Qt.LeftButton)
    mouseDrag(waitForObject(names.o_QInputDialog), 91, 54, 413, 501, 1, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem_2), 161, 51, 292, 7, 1, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem_2), 161, 51, -213, 0, 1, Qt.LeftButton)
    test.vp("VP1_move")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+C>")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+V>")
    test.vp("VP1_cv")
