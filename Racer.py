from random import *
from time import sleep
import keyboard
from threading import Timer
possibilites = ["Someone's trying to pass you, press %s to block em",
                "You've been blocked, you gotta slow down. Press down arrow",
                "You drifted too far, slow down QUICK. Press down",
                "There's a opening to the left and right of the car infront, which way?",
                "You see an opening, but its risky and you need to slow down soon or you'll crash, UP to take the opening \n DOWN to slow down",
                "There's an opening between the cars, press up arrow"]

print("Start your engines\n")
print("Get ready\n")
print("Get set\n")
print("GO! ")
input("""
-------------------------
Press enter to start""")
print(
"""
During the race, there may be several obstacles, you will have to avoid them.
You will have to be quick... waiting to long may just cause you to crash and lose the race.
Some have only one way, others can have a choice... best get into it

""")
print("You're in 5th place, wait for the oppuntnity")
position = 5
def missionfailed():
    print("You pressed the wrong button, you move in the wrong direction and crash, OUT!\n")
    return False
def timeup():
    timeup.race = False
    print("Too late, you weren't fast enough and you crashed!\n")
timeup.race = True
positioninfo = "You are now in position %d"
def challenge(arrow,move):
    global position
    if keyboard.read_key() == arrow:
        if timeup.race:
            if position != 1 and move:
                position -= 1
                print(positioninfo % position)
            print(missionpassed)
    elif timeup.race:
        timeup.race = missionfailed()
missionpassed = "Made it... lets keep at it\n"
finalstretch = True
countdown = -1
win = False
while timeup.race:
    countdown -= 1
    if position == 1 and finalstretch:
        finalstretch = False
        countdown = 5
    if countdown == 0:
        win = True
        break
    t = Timer(6,timeup)
    sleep(5)
    scenario = choice(possibilites)
    t.start()
    if scenario == possibilites[0]:
        if position != 1:
            action = choice(["left","right"])
            print(scenario % action)
            challenge(action,False)
    elif position != 1 or not scenario in possibilites[3:]:
        print(scenario)
    else:
        continue
    if scenario == possibilites[3]:
        if keyboard.read_key() == 'left' or keyboard.read_key() == 'right':
            if timeup.race:
                if randrange(1,21) == 4:
                    print("Wrong move, you scrap the other car and the car hits you off the road, taking you out of the race")
                    timeup.race = False
                    t.cancel()
                    break
                elif randint(1,10) <= 2:
                    print("Bad move, the car collides with you and pushes you back, you lost a position")
                    position += 1
                    print(positioninfo%position)
                else:
                    if position != 1:
                        position -=1 
                        print(positioninfo%position)
                    print(missionpassed)
        elif not timeup.race:
            timeup.race = missionfailed()
    elif scenario == possibilites[5]:
        challenge('up',True)
    elif scenario == possibilites[2] or scenario == possibilites[1]:
        challenge('down',False)
    elif scenario == possibilites[4]:
        if keyboard.read_key() == 'up':
            chance = randint(1,5)
            if chance == 1:
                print("Well, you hit the wall while trying to overtake and your car doesn't make it, your OUT!")
                time.uprace = False
                t.cancel()
                break
            elif chance == 2:
                print("While trying to overtake the car infront, a car knocks into you, you slow down but the damage is done, you've lost a position")
                position += 1
                print(positioninfo%position)
            else:
                if position != 1:
                    position -= 1
                    print(positioninfo%position)
                print(missionpassed)
        else:
            challenge('down',False)
    t.cancel()
if not win:
    print("\nSeems like you lost... restart the application to play again")
elif position == 1:
    print("YOU WON THE RACE IN FIRST PLACE!!! Well done, restart the application to play again")
else:
    print(f"Well done, you made it to the end of the race in place {position}... restart the application to try to get in first place.")
sleep(5)
