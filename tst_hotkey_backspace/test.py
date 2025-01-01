# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    clickButton(waitForObject(names.mainWidget_rect3_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 40, 11, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 64, 19, 103, 219, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 717, 324, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP1_before_delete")
    
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 60, 21, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.o_QInputDialog), "<Backspace>")
    test.vp("VP1_after_delete")