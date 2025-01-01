# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect4_button_QPushButton))
    clickButton(waitForObject(names.mainWidget_parallelogram_button_QPushButton))
    test.vp("VP1_before")
    mouseDrag(waitForObject(names.mainWidget_rect4_button_Canvas), 83, 31, 449, 248, 1, Qt.LeftButton)
    activateItem(waitForObjectItem(names.mainWidget_QMenuBar, "Edit"))
    activateItem(waitForObjectItem(names.mainWidget_Edit_QMenu, "Copy"))
    test.vp("VP1_select_copy")
    activateItem(waitForObjectItem(names.mainWidget_QMenuBar, "Edit"))
    activateItem(waitForObjectItem(names.mainWidget_Edit_QMenu, "Paste"))
    test.vp("VP1_paste")
