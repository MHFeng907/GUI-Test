# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    
    # 未按下按钮
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton_2).styleSheet), "")
    
    # 按下绘制直线按钮
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton_2))
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton_2).styleSheet), "background-color: lightgrey;")
    
    # 比对绘制结果
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 172, 232, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 531, 493, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem_2).pos.y, 232)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem_2).pos.x, 172)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem).pos.x, 531)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem).pos.y, 493)
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton_2).styleSheet), "background-color: lightgrey;")
    test.vp("VP10_create_line")
    
    # 取消直线绘制状态
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton_2))
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton_2).styleSheet), "background-color: white;")
