# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_parallelogram_button_QPushButton))
    test.vp("VP2_canvas_before_ctrl_x")
    test.vp("VP2_element_before_ctrl_x")
    mouseClick(waitForObject(names.rect4_button_QGraphicsPathItem_2), 73, 34, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.rect4_button_QGraphicsPathItem_2).selected, True)
    type(waitForObject(names.mainWidget_rect4_button_Canvas), "<Ctrl+X>")
    test.vp("VP2_canvas_after_ctrl_x")
    type(waitForObject(names.mainWidget_rect4_button_Canvas), "<Ctrl+V>")
    test.vp("VP2_canvas_after_ctrl_v")
    test.vp("VP2_element_after_ctrl_v")
    
    # 比较两个验证点的状态
    vp_before = test.vp("VP2_element_before_ctrl_x")  # 获取剪切前的元素验证点
    vp_after = test.vp("VP2_element_after_ctrl_v")  # 获取粘贴后的元素验证点
    test.compare(vp_before, vp_after, "The element attributes before and after Ctrl+X and Ctrl+V should be identical.")