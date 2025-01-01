# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rect2_button_QPushButton))
    test.vp("VP4_create_FlowSubElement")
