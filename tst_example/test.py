# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    clickButton(waitForObject(names.mainWidget_rect3_button_QPushButton))
    doubleClick(waitForObject(names.rect4_button_QGraphicsPathItem), 208, 129, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 152, 57, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 153, 32, 13, 202, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 542, 223, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 728, 232, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Z>")
    type(waitForObject(names.o_QInputDialog), "<Ctrl+Y>")
