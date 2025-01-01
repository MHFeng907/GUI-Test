# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_rhombus_button_QPushButton))
    test.vp("VP3_create_FlowDiamondElement")
