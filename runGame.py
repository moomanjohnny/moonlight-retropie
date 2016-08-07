#!/usr/bin/python

import os
import sys
import subprocess
import json

os.system('clear')

def execute_cmd(cmd_string):
     a = os.system(cmd_string)

def getGames():
    os.system("clear")
    gameList = subprocess.check_output(['moonlight', 'list']).split('\n')
    finishedList = []

    moonlightPath = '~/RetroPie/roms/moonlight/'

    for x in range(0, 4):
        gameList.pop(0)

    length = len(gameList) - 1
    #print(gameList)
    #print(length)

    gameList.pop(length)

    length2 = len(gameList)

    for x in range(0, length2):

        gameNum = x
        startStr = str(gameNum + 1) + ". "
        #print(startStr)
        finishedList.append(gameList[gameNum].replace(startStr, ""))
        #print(gameList[gameNum])
        #print(finishedList[gameNum])
        gamePath = os.path.join(os.path.expanduser('~'), 'RetroPie', 'roms', 'moonlight', finishedList[gameNum] + '.txt')
        gameFile = open(gamePath, 'w')
        gameFile.write(finishedList[gameNum])
        gameFile.close()
     
    os.system("clear")
    print(finishedList)

args = sys.argv

print args[1]

game = os.path.join(args[1])
configFilePath = os.path.join(args[2])

appRead = open(game, 'r')
configFile = open(configFilePath, 'r')

config = json.load(configFile)

ip = config[0]
res = config[1]
fps = config[2]
bitrate = config[3]
app = '"' + appRead.read() + '"'
mapping = args[3]


print("Running " + app)

execute_cmd("moonlight stream -" + res + " -" + fps + "fps -mapping " + mapping + " -bitrate " + bitrate + " " + " -app " + app)
getGames()

appRead.close()
configFile.close()
os.system("clear")
