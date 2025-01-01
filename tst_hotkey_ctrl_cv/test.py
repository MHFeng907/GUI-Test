# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    test.vp("VP1_canvas_before_ctrl_c")
    test.vp("VP1_element_before_ctrl_c")
    
    mouseClick(waitForObject(names.mainWidget_rect4_button_Canvas), 304, 68, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsPathItem_2).selected, False)
    
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 169, 36, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsPathItem_2).selected, True)

    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 187, 56, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWidget_rect4_button_Canvas), "<Ctrl+C>")
    type(waitForObject(names.mainWidget_rect4_button_Canvas), "<Ctrl+V>")
    
    test.vp("VP1_canvas_after_ctrl_cv")
    test.vp("VP1_element_after_ctrl_cv")
    test.vp("VP1_new_element_after_ctrl_cv")
    
    
    # 比较两个验证点的状态
    vp_before = test.vp("VP1_element_before_ctrl_c")  # 获取复制前的元素验证点
    vp_after = test.vp("VP1_element_after_ctrl_cv")  # 获取粘贴后的元素验证点
    test.compare(vp_before, vp_after, "The element attributes before and after Ctrl+C and Ctrl+V should be identical.")
