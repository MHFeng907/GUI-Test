# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_roundrect_button_QPushButton))
    test.vp("VP8_create_FlowRadiusElement")
