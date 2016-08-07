#!/usr/bin/python

import os
import sys
import imp
import subprocess


try:
    dialogSource = sys.argv[1]
except IndexError:
    print("Could not find dependency dialog.py. Exiting with error code 1.")
    sys.exit(1)

dialog = imp.load_source("dialog", dialogSource)
d = dialog.Dialog(dialog="dialog")
d.set_background_title("Moonlight Embedded Post Install Configurator by Johnny Panos")

d.msgbox("Welcome to the Moonlight Embedded for RetroPie Post Install Configurator!\n\nThis will configure your controller for use with Moonlight.", width=70, height=8)

os.system('clear')
print("The GUI has been disabled for this step, because it would interfere with the controller configuration.\n\nJust follow the onscreen instructions.\n")
os.system("moonlight map /opt/retropie/configs/moonlight/controller.map")

d.msgbox("Controller configuration saved.\n\nPress 'OK' to continue.", width=70, height=7)
d.msgbox("The only thing left is for you to pair your computer to moonlight.\n\nType 'moonlight pair [your computers ip]' into a terminal to pair them.", width=70, height=8)
os.system("clear")


