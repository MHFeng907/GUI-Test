# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 221, 67, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 158, 339, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_parallelogram_button_QPushButton))
    mouseClick(waitForObject(names.o_QInputDialog), 426, 606, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 91, 51, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 75, 35, 94, 330, 1, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 501, 466, Qt.NoModifier, Qt.LeftButton)
    
    # 吸附点大致坐标
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 157, 35, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 136, 95, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsRectItem_9), 3, -1, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 91, 53, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsRectItem_7), 2, 2, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.o_QInputDialog), 550, 318, Qt.NoModifier, Qt.LeftButton)
    
    # 绘制
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 152, 90, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 62, 6, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP1_after")
    
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 76, 39, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 73, 36, 126, 41, 1, Qt.LeftButton)
    test.vp("VP1_move_verify")
