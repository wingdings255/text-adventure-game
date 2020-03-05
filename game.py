#!/usr/bin/python
import os
import time

global ostype
ostype = os.name

global clearcmd
if ostype == "nt":
    clearcmd = 'cls'
elif ostype == "posix":
    clearcmd = 'clear'

global gold
gold = 100

global inv
inv = ["Rusty Sword", ]

global quests
quests = ["Test", ]

global eggs
eggs = 0

global name

os.system(clearcmd)
print("Halt! Who goes there? State your name.")
name = input("Enter your name:  ")
print("Welcome to Audale " + name)
time.sleep(3)


def start():
    global name
    global clearcmd
    global gold
    os.system(clearcmd)
    if name == "garet":
        thief_easteregg()
    print("As you enter the town you look around at the shops and booths.")
    print("A fish monger runs up to you and ask's if you want to buy a fish")
    print("He wreaks of dead fish so you can assume his stock cant be the best")
    print("you have" + " " + str(gold) + " " + "gold")
    print("----------------------")
    time.sleep(4)
    print(" ")
    print("1). Accept the fish")
    print("->  Costs 5 gold")
    print(" ")
    print("2). Decline the fish")
    # TODO: add and else that loops back to the original question
    ans = input("1 or 2: ")
    if ans == "1":
        sequence1_section2_yes()
    if ans == "2":
        sequence1_section2_no()


def death():
    global gold
    global eggs
    global name
    print("----------------------")
    time.sleep(1)
    print(name + " HAS DIED!!! R.I.P")
    time.sleep(1)
    print("----------------------")
    time.sleep(1)
    if str(eggs) >= "0":
        print("You finished with " + str(eggs) + " " + "eastereggs")
        time.sleep(1)
        print("You finished with " + str(gold) + " gold")
    time.sleep(3)
    quit()


def sequence1_section2_yes():
    global gold
    global inv
    os.system(clearcmd)
    print("Thank you for your purchase" + " " + name)
    print("The fishmonger takes 5 gold and gives you the fish")
    inv.append("Fish")
    gold = gold - 5
    print("<<you now have" + " " + str(gold) + " " + "gold>>")
    time.sleep(2)
    for x in inv:
        print("----------------------")
        print("Your inventory is:" + " " + x)
    quests.append("Bear")
    print("----------------------")
    time.sleep(2)
    print("!Your quests have been updates. Visit the Tavern to see avalible quests!")
    time.sleep(6)
    sequence2_section1()


def sequence1_section2_no():
    global eggs
    os.system(clearcmd)
    print("The fishmonger stabs you in the neck and you die")
    time.sleep(2)
    death()


def thief_easteregg():
    global eggs
    print("----------------------")
    print("!!Congrats, you found an easteregg!!")
    eggs = eggs + 1
    print("!!you now have discovered" + " " + "<" + str(eggs) + ">" + " " + "eastereggs!!")
    print("----------------------")


def sequence2_section1():
    global clearcmd
    os.system(clearcmd)
    print("You place your fish in your bag and continue riding through the town")
    print("As you ride through the town, you hear a loud crash and men yelling.")
    print("You correctly assume it is a tavern.")
    print("----------------------")
    print("Would you like to enter the tavern??")
    print("1).  Yes")
    print("2).  No")
    ans = input("1 or 2: ")
    if ans == "1":
        print("You ride up and tether your horse to a pole and head on in")
        time.sleep(4)
        tavern()
    else:
        quit()


def tavern():
    global name
    global gold
    global quests
    os.system(clearcmd)
    print("Welcome to the Tavern " + name + " would you like to view quests?")
    time.sleep(1)
    print("")
    print("1). yes")
    print("")
    print("2.) no")
    ans = input("1 or 2: ")
    if ans == "1":
        print("You have [" + str(len(quests)) + "] quests")
        questchoose()
    elif ans == "2":
        print("What do you mean no? this is literally the only thing you can do in the tavern so far")
        tavern()


def questchoose():
    global quests
    global name
    os.system(clearcmd)
    print("You have [" + str(len(quests)) + "] quests")
    time.sleep(3)
    for x in quests:
        print("Quest: " + x)
    ans = input("What quest do you want to begin:   ")
    if ans == quests[0]:
        print("you have chosen the " + quests[0] + " quest")
        time.sleep(2)
        quest_bear()
    else:
        print("Quest not found")
        questchoose()


def quest_bear():
    global name
    print("Thank you for accepting this quest " + name)
    print("There is a large bear that is terorizing our hunters in the woods outside the village")
    print("You will be paid hansomly to take care of this pest")
    print("You leave the Tavern and make your way to the bears cave")
    time.sleep(2)


start()
