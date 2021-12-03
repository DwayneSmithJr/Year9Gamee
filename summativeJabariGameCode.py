import playsound
import time 
import termcolor 
import sys
from pygame import mixer
from typeWriter import typewrite 

mixer.init() #Initialzing pyamge mixer
mixer.music.load('jeopardy.mp3') #Loading Music File
baseValues = [0]
characterTraits =["courage"]
checkpoints = [4.5]
## Inital Text
playerName= input("Welcome Challenger: \nPlease Input Your Name \n")
typewrite("Welcome to the Parallel World of Jabari, "), typewrite(playerName), typewrite(". This is an alternate world to what you know. Get ready for a whole new experience \n")
typewrite("INSTRUTIONS\n\nThere is going to be a series of questions testing your level of courage. \n There will be 6 different questions, 3 Main and 3 Side. \n The Main Questions are worth 2 points and the Side questions will be worth 1 point.\n There is also two correct answers for every question. One will be worth half and the other will be for full points.\n ")
typewrite("I hope you're ready!!")
print()

## Access Token link: 

def CheckProgress():
    global baseValues,characterTraits,checkpoints
    i = 0


    pointsUntilCheckpoint= checkpoints[0] - baseValues[0]

    while i < 1:
        time.sleep(3)
        print("You currently have:\n",baseValues[i],characterTraits[i],"\nYou need to get to: \n",checkpoints[i], characterTraits[i])
        if baseValues[0] >= checkpoints[0]:
            print ("You win")
        else:
            print("you need: ", pointsUntilCheckpoint, "more courage points "  )

        i += 1
CheckProgress()
correct = False 
while not correct:
    moraleChecker= input("Here comes the First Side Question: \n Are you Ready, Yes or No?:\n")
    if 'yes' in moraleChecker.lower():
        correct = True
    else:
        print ("Okay, come back, when you're ready!\n \n ")
print ('All right here we go!\n') 
## Getting Ready to do the first sub question 
mixer.music.play("jeopardy.mp3")
typewrite("So you are driving to the swimming pool and your parents ask: \n What do you want to do when you get there? \n a) talk to the other kids there?\n b) casually swim\n c) jump off the diving board\n ")

side1 = input()
if side1.lower() == "a":
    print ("Come on you can be more courageous than that") 
elif side1.lower() == "b":
    print("Good job but you got the half answer. There is a more courageous answer")
    baseValues[0] += 0.5
    print ("You will get 0.5 courage points for this")
else:
    print("Good job, i'm impressed by your courage. You will get full points for this display of courage") 
    baseValues[0] += 1 
    print ("You will get 1 courage point for this")
mixer.music.stop("jeopardy.mp3")
CheckProgress()

typewrite("Good Job for answering that for sub question. Here comes a Main Question ")

typewrite("So you are about to get to the pool: \n What's your goal \n a) Climb up the ladder to get to the diving board \n b) running into a jump in the pool \n c) run across the deck\n ")
main1 = input()
if main1.lower() == "a":
    print("Good job, i'm impressed by your courage. You will get full points for this display of courage") 
    baseValues[0] += 1 
    print ("You will get 1 courage point for this")
elif main1.lower() == "b":
    print("Good job but you got the half answer. There is a more courageous answer")
    baseValues[0] += 0.5
    print ("You will get 0.5 courage points for this")
else:
    print ("Come on you can be more courageous than that") 
CheckProgress()

typewrite("You didn't have enough courage to jump off the diving board so you went back down the ladder. ")
typewrite("You go back to your parents after what happened.: \n what will you tell them? \n a) I jumped off the diving board with no difficulty \n b) I was too scared to jump off the diving board. \n c) I almost jumped off the diving board\n ")
side2 = input()
if side2.lower() == "a":
    print ("That was a lie and was not courageous at all. ") 
elif side2.lower() == "b":
    print("You are a master at courage, truly well done!") 
    baseValues[0] += 1 
    print ("You will get 1 courage point for this")
else:
    print("Good job but you got the half answer. There is a more courageous answer")
    baseValues[0] += 0.5
    print ("You will get 0.5 courage points for this")
CheckProgress()
typewrite("You eventually start to walk in the direction off the ladder again.")
typewrite("You have reached the base: \n what will you do? \n a) gather up the courage to climb up the ladder. \n b) talk to another kid about battleships \n c) think about how you're going to jump off\n ")
main2 = input()
if main2.lower() == "a":
    print("Good job, you're displaying the qualities of a champion. You will get full points ") 
    baseValues[0] += 1 
elif main2.lower() == "b":
    print ("Come on you can be more courageous than that") 
else:
    print("Good job but you got the half answer. There is a more courageous answer")
    baseValues[0] += 0.5
    print ("You will get 0.5 courage points for this")

CheckProgress()
