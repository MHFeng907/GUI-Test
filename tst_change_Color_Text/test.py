# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    doubleClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 303, 157, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP2_before_change_text")
    clickButton(waitForObject(names.mainWidget_color_button_QPushButton))
    mouseClick(waitForObject(names.basic_colors_QtPrivate_QWellArray), 42, 85, Qt.NoModifier, Qt.LeftButton)
    
    # 获取 QLineEdit 中的颜色文本
    color_from_lineedit = str(waitForObjectExists(names.qt_colorname_lineedit_QLineEdit_2).text).strip().lower()

    clickButton(waitForObject(names.select_Color_OK_QPushButton))

    # 获取 GraphicsTextItem 的默认文本颜色
    color_from_graphicstextitem = str(waitForObjectExists(names.rect4_button_Text_here_GraphicsTextItem).defaultTextColor.name).strip().lower()

    # 比较两个颜色值是否相等
    test.compare(color_from_lineedit, color_from_graphicstextitem)
    
    test.vp("VP2_after_change_text")


