from typeWriter import typewrite


import playsound
import time 
import termcolor 
import sys


playerName= input("Please Input Your Name \n")
typewrite("Welcome to the Parallel world of Jabari, "), typewrite(playerName), typewrite(".This is an alternate world to what you know. Get ready to experience a whole new world!")



def CheckProgress():
    i = 0

    baseValues = [0]
    characterTraits = ["courage"]
    checkpoints = [8]
    pointsUntilCheckpoint= checkpoints[i] - baseValues[i]

    while i < 1:
        time.sleep(3)
        print("You currently have:\n",baseValues[i],characterTraits[i],"\nYou need to get to: \n",checkpoints[i], characterTraits[i])
        if baseValues[0] == checkpoints[0]:
            print ("You win")
        else:
            print("you need: ", pointsUntilCheckpoint, "more points "  )

        i += 1

CheckProgress()

