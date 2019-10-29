#!/usr/bin/python
import json
import random
import os
import time

global gold
gold = 100

global inv
inv = []

global quests
quests = []

global eggs
eggs = 0

global name

print("Halt! Who goes there? State your name.")
name=input()
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
    print("you have" +" " + str(gold) + " "+"gold")
    print("---------------------------------------------------------------")
    print(" ")
    print("1). Accept the fish")
    print("Costs 5 gold")
    print(" ")
    print("2). Decline the fish")
    ans=input()
    if ans == "1":
        sequence1_section2_yes()
    if ans == "2":
        sequence1_section2_no()



def sequence1_section2_yes():
    global gold
    global inv
    os.system('clear')
    print("Thank you for your purchase" + " "  + name)
    print("The fishmonger takes 5 gold and gives you the fish")
    inv.append("Fish")
    gold = gold - 5
    print("<<you now have" + " " + str(gold) +  " " + "gold>>" )
    for x in inv:
      print("<<Your inventory is:" + " " + x + " " + ">>")
    quests.append("bear")
    print("!Your quests have been updates. Visit the Tavern to see avalible quests!")
    time.sleep(5)
    sequence2_section1()

def sequence1_section2_no():
    global eggs
    os.system('clear')
    print("The fishmonger stabs you in the neck and you die")
    print("----------------------")
    print("YOU HAVE DIED!!! R.I.P")
    print("----------------------")
    #if int(eggs) >= "1":
    #    print("you have finished with" + str(eggs) + "easter eggs discovered")
    quit()

def thief_easteregg():
        print ("--------------------------------------")
        print ("!!Congrats, you found an easteregg!!")
        global eggs
        eggs = eggs+1
        print("!!you now have discovered" + " " + "<" +  str(eggs) + ">" +  " "  + "eastereggs!!")
        print("-----------------------------------------------------------------")

def sequence2_section1():
    os.system('clear')
    print("You place your fish in your bag and continue riding through the town")

def tavern ():
    global name
    global gold
    global quests



start()
