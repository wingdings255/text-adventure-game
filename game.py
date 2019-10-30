#!/usr/bin/python
import os
import time

global gold
gold = 100

global inv
inv = ["Rusty Sword", ]

global quests
quests = ["Test", ]

global eggs
eggs = 0

global name

print("Halt! Who goes there? State your name.")
name = input("Enter your name:  ")
print("Welcome to Audale " + name)
time.sleep(3)


def start():
    global name
    global gold
    os.system('clear')
    if name == "garet":
        thief_easteregg()
    print("As you enter the town you look around at the shops and booths.")
    print("---------------------------------------------------------------")
    print("A fish monger runs up to you and ask's if you want to buy a fish")
    print("He wreaks of dead fish so you can assume his stock cant be the best")
    print("you have" + " " + str(gold) + " " + "gold")
    print("---------------------------------------------------------------")
    print(" ")
    print("1). Accept the fish")
    print("Costs 5 gold")
    print(" ")
    print("2). Decline the fish")
    # TODO: add and else that loops back to the original question
    ans = input()
    if ans == "1":
        sequence1_section2_yes()
    if ans == "2":
        sequence1_section2_no()


def death():
    global gold
    global eggs
    global name
    print("----------------------")
    print(name + " HAS DIED!!! R.I.P")
    print("----------------------")
    if str(eggs) >= "0":
        print("You finished with " + str(eggs) + " " + "eastereggs")
        print("You finished with " + gold + " gold")
    quit()


def sequence1_section2_yes():
    global gold
    global inv
    os.system('clear')
    print("Thank you for your purchase" + " " + name)
    print("The fishmonger takes 5 gold and gives you the fish")
    inv.append("Fish")
    gold = gold - 5
    print("<<you now have" + " " + str(gold) + " " + "gold>>")
    for x in inv:
        print("<<Your inventory is:" + " " + x + " " + ">>")
    quests.append("Bear")
    print("!Your quests have been updates. Visit the Tavern to see avalible quests!")
    time.sleep(5)
    sequence2_section1()


def sequence1_section2_no():
    global eggs
    os.system('clear')
    print("The fishmonger stabs you in the neck and you die")
    time.sleep(2)
    death()


def thief_easteregg():
    global eggs
    print ("--------------------------------------")
    print ("!!Congrats, you found an easteregg!!")
    eggs = eggs+1
    print("!!you now have discovered" + " " + "<" + str(eggs) + ">" + " " + "eastereggs!!")
    print("-----------------------------------------------------------------")


def sequence2_section1():
    os.system('clear')
    print("You place your fish in your bag and continue riding through the town")
    print("As you ride through the town, you hear a loud crash and men yelling.")
    print("You correctly assume it is a tavern.")
    print("You ride up and tether your horse to a pole and head on in")
    tavern()


def tavern():
    global name
    global gold
    global quests
    print("Welcome to the Tavern " + name + " would you like to view quests?")
    print("")
    print("1). yes")
    print("")
    print("2.) no")
    ans = input()
    if ans == "1":
        print("Your you have [" + str(len(quests)) + "] quests")
        time.sleep(3)
        for x in quests:
            print("Quest: " + x)
        ans = input("What quest do you want to begin:   ")
        if ans == quests[1]:
            print("you have chosen the " + quests[1] + " quest")
            quest_bear()
        elif ans == quests[2]:
            print("This is a test quest and does not exist")
    elif ans == "2":
        print("What do you mean no? this is literally the only thing you can do in the tavern so far")
        tavern()


def quest_bear():
    print("Thank you for accepting this quest " + name)


start()
