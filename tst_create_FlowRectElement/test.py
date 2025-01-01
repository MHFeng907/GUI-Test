# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect_button_QPushButton))
    test.vp("VP6_create_FlowRectElement")
