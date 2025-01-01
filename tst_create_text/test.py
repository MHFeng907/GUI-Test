# -*- coding: utf-8 -*-

import names

# element 关键坐标
top_left = (200, 100)  # 左上角坐标
bottom_right = (400, 200)  # 右下角坐标

# 判断一个点是否在矩形区域内
def is_point_in_rectangle(x, y, top_left, bottom_right):
    return top_left[0] <= x <= bottom_right[0] and top_left[1] <= y <= bottom_right[1]

def main():
    startApplication("FlowelementChart")
    test.vp("VP11_before_create_text_in_canvas")
    
    # 模拟双击创建文本并验证位置
    doubleClick(waitForObject(names.mainWidget_rect4_button_Canvas), 328, 227, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP11_after_create_text_in_canvas")
    test.vp("VP11_new_text_in_canvas")
    
    # 获取新建文本的坐标并进行四舍五入验证
    new_text_item = waitForObject(names.rect4_button_Text_here_GraphicsTextItem)
    text_x = new_text_item.pos.x
    text_y = new_text_item.pos.y
    test.compare(round(text_x), 328)  # 四舍五入到整数
    test.compare(round(text_y), 227)  # 四舍五入到整数

    # 在图形内创建文本
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    test.vp("VP11_before_create_text_in_element")
    
    # 模拟双击图形元素创建文本并验证位置
    doubleClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 205, 149, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP11_after_create_text_in_element")
    
    # 获取新建文本的坐标并进行四舍五入验证
    new_text_item_2 = waitForObject(names.rect4_button_Text_here_GraphicsTextItem_2)
    text_x_2 = new_text_item_2.pos.x
    text_y_2 = new_text_item_2.pos.y
    test.compare(round(text_x_2), 253)  # 四舍五入到整数
    test.compare(round(text_y_2), 132)  # 四舍五入到整数

    # 检查新建文本坐标是否在矩形区域内
    assert is_point_in_rectangle(text_x_2, text_y_2, top_left, bottom_right), \
        f"Text position ({text_x_2}, {text_y_2}) is outside the rectangle."
    
