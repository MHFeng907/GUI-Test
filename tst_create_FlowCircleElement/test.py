# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_circle_button_QPushButton))
    test.vp("VP7_create_FlowCircleElement")
