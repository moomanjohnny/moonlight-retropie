#!/usr/bin/python

import imp
import os
import sys
import subprocess

try:
    dialogSource = sys.argv[4]
except IndexError:
    print("Could not find dependency dialog.py. Exiting with error code 1.")
    sys.exit(1)

dialog = imp.load_source("dialog", dialogSource)

try:
    configFile = sys.argv[1]
except IndexError:
    d = dialog.Dialog(dialog="dialog")
    d.set_background_title("Error")

    d.msgbox("Could not find config.py executable. Please reinstall moonlight from the retropie package manager.")
    sys.exit(1)

try:
    configFileDir = sys.argv[2]
except IndexError:
    d = dialog.Dialog(dialog="dialog")
    d.set_background_title("Error")

    d.msgbox("Could not find config.cfg. Please reinstall moonlight from the retropie package manager.")
    sys.exit(1)

try:
    title = sys.argv[3]
except IndexError:
    title = "Configure moonlight"

res1080 = False
res720 = True

currentRes = ""
currentRefresh = ""

configExecutable = os.path.join(configFile)
process = subprocess.Popen([configExecutable, '-config', configFileDir, '-getResolution'], stdout=subprocess.PIPE)
out = process.communicate()
if out[0] == "1080\n":
    res1080 = True
    currentRes = "1080p"
elif out[0] == "720\n":
    res720 = True
    currentRes = "720p"

process2 = subprocess.Popen([configExecutable, '-config', configFileDir, '-getRefresh'], stdout=subprocess.PIPE)
out2 = process2.communicate()
if out2[0] == "60\n":
    currentRefresh = "60fps"
elif out2[0] == "30\n":
    currentRefresh = "30fps"

d = dialog.Dialog(dialog="dialog")
d.set_background_title(title)

def setRes():
    global currentRes
    choices = [
        ('1080p', '- Sets the resolution to 1920x1080.'),
        ('720p', '- Sets the resolution to 1280x720.')
        ]

    while True:
        code, tag = d.menu("Please select a resolution.\n\nCurrent resolution: " + currentRes, height=23, width=76,
                choices=choices)

        if code == "ok":
            print tag
            setConfig = subprocess.Popen([configExecutable, '-config', configFileDir, '-resolution', tag], stdout=subprocess.PIPE)
            currentRes = tag
            print(setConfig)
            break
        elif code == "cancel":
            break

def setBitrate():
    code, answer = d.inputbox("Enter bitrate in kbps.", init="10000")
    if code == "ok":
            print answer
            setConfig = subprocess.Popen([configExecutable, '-config', configFileDir, '-bitrate', answer], stdout=subprocess.PIPE)
            print(setConfig)

def setRefresh():
    global currentRefresh
    choices = [
        ('60fps', '- Sets the refresh rate to 60fps.'),
        ('30fps', '- Sets the refresh rate to 30fps.')
        ]

    while True:
        code, tag = d.menu("Please select a refresh rate.\n\nCurrent refresh rate: " + currentRefresh, height=23, width=76,
                choices=choices)

        if code == "ok":
            print tag
            setConfig = subprocess.Popen([configExecutable, '-config', configFileDir, '-refresh', tag], stdout=subprocess.PIPE)
            currentRefresh = tag
            print(setConfig)
            break
        elif code == "cancel":
            break

#setBitrate()
choices = [
    ('1', '- Set the streaming resolution.'),
    ('2', '- Set the streaming refresh rate.'),
    ('3', '- Set the streaming bitrate.')
    ]

while True:
    code, tag = d.menu("Please select an option.", height=23, width=76,
            choices=choices)

    if code == "ok":
        if tag == '1':
            setRes()
        elif tag == '2':
            setRefresh()
        elif tag == '3':
            setBitrate()
    elif code == "cancel":
        break
