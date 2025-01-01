# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    test.vp("VP3_before_change_element")
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 136, 46, Qt.NoModifier, Qt.LeftButton)
    
    # 改变填充颜色
    clickButton(waitForObject(names.mainWidget_color_button_QPushButton))
    mouseClick(waitForObject(names.basic_colors_QtPrivate_QWellArray), 102, 81, Qt.NoModifier, Qt.LeftButton)
    
    # 获取 QLineEdit 中的颜色值并进行比较
    color_from_lineedit = str(waitForObjectExists(names.qt_colorname_lineedit_QLineEdit_2).text).strip().lower()
    test.compare(color_from_lineedit, "#ff5500")
    
    # 确认颜色并保存
    clickButton(waitForObject(names.select_Color_OK_QPushButton))
    test.vp("VP3_after_change_inner")
    
    # 获取 QGraphicsPathItem 的颜色值并进行比较
    color_from_graphicspathitem = str(waitForObjectExists(names.rect4_button_QGraphicsPathItem_7).brush.color.name).strip().lower()
    test.compare(color_from_graphicspathitem, "#ff5500")
    
    # 颜色比对 
    test.compare(color_from_graphicspathitem, color_from_lineedit)
    
    # 改变边框颜色
    clickButton(waitForObject(names.mainWidget_border_color_button_QPushButton))
    mouseClick(waitForObject(names.basic_colors_QtPrivate_QWellArray_2), 183, 10, Qt.NoModifier, Qt.LeftButton)
    
    # 获取 QLineEdit 中的边框颜色值并进行比较
    color_from_lineedit_border = str(waitForObjectExists(names.qt_colorname_lineedit_QLineEdit).text).strip().lower()
    test.compare(color_from_lineedit_border, "#00ff00")
    
    # 确认边框颜色并保存
    clickButton(waitForObject(names.select_Border_Color_OK_QPushButton))
    test.vp("VP3_after_change_out")
    
    # 获取 QGraphicsPathItem 边框颜色并进行比较
    color_from_graphicspathitem_border = str(waitForObjectExists(names.rect4_button_QGraphicsPathItem_8).pen.color.name).strip().lower()
    test.compare(color_from_graphicspathitem_border, "#00ff00")
    
    # 颜色比对 
    test.compare(color_from_graphicspathitem_border, color_from_lineedit_border)
