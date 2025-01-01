# -*- coding: utf-8 -*-

import names


def main():
    startApplication("FlowelementChart")
    activateItem(waitForObjectItem(names.mainWidget_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.mainWidget_File_QMenu, "Exit"))
