# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    
    # 按钮未被按下
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton).styleSheet), "")
    
    # 按钮按下变灰
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton).styleSheet), "background-color: lightgrey;")
    
    # 箭头起点终点位置检验
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 187, 250, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 393, 207, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem_2).pos.x, 187)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem_2).pos.y, 250)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem).pos.x, 393)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsRectItem).pos.y, 207)
    test.vp("VP9_create_arrow")
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton).styleSheet), "background-color: lightgrey;")
    
    # 结束绘制箭头状态
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    test.compare(str(waitForObjectExists(names.mainWidget_arrow_button_QPushButton).styleSheet), "background-color: white;")
