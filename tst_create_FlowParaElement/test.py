# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    clickButton(waitForObject(names.mainWidget_parallelogram_button_QPushButton))
    test.vp("VP5_create_FlowParaElement")
