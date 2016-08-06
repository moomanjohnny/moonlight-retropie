#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import all the crap
import os
import subprocess
import sys
import json

# Get args from terminal.
args = sys.argv

# Set variables to placeholder values.
configFilePath = ""
configFileRead = ""
configFileWrite = ""

oldConfig = []
newConfig = []

configLoaded = False

def isLoaded():
    if configLoaded == False:
        sys.exit("No config file specified, please use '-config' to specify a config file.")

def loadConfig(argNum):
    global configLoaded
    global configFilePath
    global configFileRead
    global configFileWrite

    global oldConfig
    global newConfig

    # Load config file from path given from args.
    try:
        configFilePath = os.path.join(args[argNum + 1])
    except IndexError:
        sys.exit("Config file not specified after -config, try again.")

    # TODO: Make it when it saves the config, it makes a .bak of the old config file.
    configFileRead = open(configFilePath, 'r')

    try:
        oldConfig = json.load(configFileRead)
    except ValueError:
        sys.exit("Could not parse config file. Is it in JSON format?")
    
    newConfig = oldConfig
    configFileRead.close()
    
    configFileWrite = open(configFilePath, 'w')

    # Set to true so the program knows we loaded the config file.
    configLoaded = True

def setRes(argNum):
    # Check to see if the config file is loaded.
    isLoaded()

    try:
        resArg = args[argNum + 1]
    except IndexError:
        sys.exit("Please specify either 1080 or 720 for -resolution")

    global newConfig
    if resArg == "1080p":
        newConfig[1] = "1080"
    elif resArg == "720p":
        newConfig[1] = "720"
    else:
        # Exit if the input is invalid.
        sys.exit("Please use only '1080p' or '720p' for the '-resolution' option.")

def getResolution():
    isLoaded()

    print(newConfig[1])

def setRefresh(argNum):
    # Check to see if the config file is loaded.
    isLoaded()

    try:
        resArg = args[argNum + 1]
    except IndexError:
        sys.exit("Please specify either 60fps or 30fps for -refresh.")

    global newConfig
    if resArg == "60fps":
        newConfig[2] = "60"
    elif resArg == "30fps":
        newConfig[2] = "30"
    else:
        sys.exit("Please only use '60' or '30' for the '-refresh' option")

def getRefresh():
    isLoaded()

    print(newConfig[2])
    
def setBitrate(argNum):
    # Check to see if the config file is loaded.
    isLoaded()

    try:
        resArg = args[argNum + 1]
    except IndexError:
        sys.exit("Please specify a bitrate for the -bitrate option.")

    global newConfig
    newConfig[3] = resArg

def displayHelp():
    print("Moonlight for RetroPie Configurator v0.0.5\nUsage: ./config.py [action] (setting)\nActions:\n-config\tSpecify a path to the config file.\n-resolution\tSpecify resolution setting, use either 1080 or 720\n-refresh\tSpecify refresh rate, use either 60 or 30\n-bitrate\tSpecify a bitrate in kbps. (Do not put kbps at the end.)\n-help\tDisplays this message")

for x in range(1, len(args)):

    # Handle args
    if args[x] == "-config":
        loadConfig(x)
    elif args[x] == "-resolution":
        setRes(x)
    elif args[x] == "-refresh":
        setRefresh(x)
    elif args[x] == "-bitrate":
        setBitrate(x)
    elif args[x] == "-help":
        displayHelp()
    elif args[x] == "-getResolution":
        getResolution()
    elif args[x] == "-getRefresh":
        getRefresh()
    else:
        configLoaded = configLoaded

if configLoaded == True:
        json.dump(newConfig, configFileWrite)
        configFileWrite.close()
