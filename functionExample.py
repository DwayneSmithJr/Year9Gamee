#Dwayne Smith Jr. 
#December 2nd, 2021
#It is a progress checker to find how much courage points you have

#It only works with courage points
#you have to declare baseValues, characterTraits and checkpoints beforehand
#Either you win or it tells you how much more you need
#you need: you need ", "pointsUntilCheckpoint, "more courage points " or "you have: ", pointsAboveCheckpoint, "extra courage points "  
import time
baseValues = [0]
characterTraits =["courage"]
checkpoints = [2.5]

def CheckProgress():
    global baseValues,characterTraits,checkpoints
    i = 0
    pointsAboveCheckpoint= baseValues[0] - checkpoints[0]
    pointsUntilCheckpoint= checkpoints[0] - baseValues[0]
    while i < 1:
        time.sleep(3)
        print("You currently have:\n",baseValues[i],characterTraits[i],"\nYou need to get to: \n",checkpoints[i], characterTraits[i])
        if baseValues[0] == checkpoints[0]:
            print ("You win")
        elif baseValues[0] >= checkpoints[0]:
            print ("You've beat the required amount of courage points")
            print("you have: ", pointsAboveCheckpoint, "extra courage points "  )
        else:
            print("you need: ", pointsUntilCheckpoint, "more courage points "  )

        i += 1