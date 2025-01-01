# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    clickButton(waitForObject(names.mainWidget_rhombus_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem), 112, 48, Qt.NoModifier, Qt.LeftButton)
    dragItemBy(waitForObject(names.rect4_button_QGraphicsPathItem), 128, 35, 51, 211, 1, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 133, 100, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 304, 312, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_arrow_button_QPushButton))
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 630, 359, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP1_before_change_line")
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsPathItem_3).brush.style, 0)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsPathItem_3).pen.width, 3)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsPathItem_3).pen.capStyle, 16)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsPathItem_3).pen.joinStyle, 64)
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_3), 5, 54, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWidget_border_color_button_QPushButton))
    mouseClick(waitForObject(names.basic_colors_QtPrivate_QWellArray_2), 44, 89, Qt.NoModifier, Qt.LeftButton)
    
    # 获取 QLineEdit 中的颜色文本
    color_from_lineedit = str(waitForObjectExists(names.qt_colorname_lineedit_QLineEdit).text)
    
    clickButton(waitForObject(names.select_Border_Color_OK_QPushButton))
    
    # 获取 QGraphicsPathItem 的笔触颜色
    color_from_graphicspathitem = str(waitForObjectExists(names.rect4_button_QGraphicsPathItem_6).pen.color.name)

    test.vp("VP1_after_change_line")
    
    # 比较两个颜色值是否相等
    test.compare(color_from_lineedit, color_from_graphicspathitem)
