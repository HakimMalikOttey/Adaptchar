import os, sys
import yaml
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import time
import platform
#Defines the actions that each bot can take in the game. Goes as...Action[Damage, Damage type]
#Defines what kind of bot is present. PL - Player/ Player bots. EN - Enemy bots
## Start of Player 1 Information
comp1_Attacks = {'ATK': [20, 'NORMAL'], 'ICE':[30,'ICE'],'FIRE': [40,'FIRE']}
comp1_Stats = {'WEAKNESS': ['ICE',100], 'HP': 400000, 'TYPE':"PL"}
#Stores the values for
one_val = list(comp1_Attacks.values())
one_key = list(comp1_Attacks.keys())
one_stat_val = list(comp1_Stats.values())
one_stat_key = list(comp1_Stats.keys())
###
##Start of Bot 2 Information (Bot 1 is player)
comp2_Attacks = {'ATK': [20, 'NORMAL'], 'ICE':[30,'ICE'],'FIRE': [40,'FIRE'],'TYPE':"PL"}
comp2_Stats = {'WEAKNESS': ['ICE',100], 'HP': 400000, 'TYPE':"PL"}
two_val = list(comp2_Attacks.values())
two_key = list(comp2_Attacks.keys())
two_stat_val = list(comp2_Stats.values())
two_stat_key = list(comp2_Stats.keys())
###
##Start of Bot 3 Information
comp3_Attacks = {'ATK': [20, 'NORMAL'], 'ICE':[30,'ICE'],'FIRE': [40,'FIRE'],'TYPE':"PL"}
comp3_Stats = {'WEAKNESS': ['ICE',100], 'HP': 400000, 'TYPE':"PL"}
three_val = list(comp3_Attacks.values())
three_key = list(comp3_Attacks.keys())
three_stat_val = list(comp3_Stats.values())
three_stat_key = list(comp3_Stats.keys())
##
##Start of Bot 4 Information
comp4_Attacks = {'ATK': [20, 'NORMAL'], 'ICE':[30,'ICE'],'FIRE': [40,'FIRE'], 'TYPE':"PL"}
comp4_Stats = {'WEAKNESS': ['ICE',100], 'HP': 400000, 'TYPE':"PL"}
four_val = list(comp4_Attacks.values())
four_key = list(comp4_Attacks.keys())
four_stat_val = list(comp4_Stats.values())
four_stat_key = list(comp4_Stats.keys())
##
##Start of Enemy Information
ENEM_Attacks = {'ATK': [20, 'NORMAL'], 'ICE':[30,'ICE'],'FIRE': [40,'FIRE'], 'TYPE':"PL"}
ENEM_Stat = {'WEAKNESS': ['ICE',100], 'HP': 400000, 'TYPE':"EN"}
EN_val = list(ENEM_Attacks.values())
EN_key = list(ENEM_Attacks.keys())
EN_stat_val = list(ENEM_Stat.values())
EN_stat_key = list(ENEM_Stat.keys())
##
done = False
turn = 1
overall = ""
def DMG_Effect(a):
    dmg = ENEM_Stat['HP'] - a
    ENEM_Stat['HP'] = dmg
    print("Enemy now has",ENEM_Stat['HP'], "HP")
def fileopen(a,b):
    opener = open(a,'a')
    with open(a,'a') as yaml_file:
        yaml.dump(str(b).replace("'", ""), yaml_file,default_flow_style = True)
    opener.close()
while not done:
    if turn == 5:
        turn = 1
    if turn == 1:
        print("What attack do you want to do?")
        for key, value in comp1_Attacks.items():
            print(key)
        user = input()
        if comp1_Attacks[user][1] == ENEM_Stat['WEAKNESS'][0]:
            overall =   ENEM_Stat["WEAKNESS"][1] + comp1_Attacks[user][0]
            response = "- - PLAYER used " + user +  " on the enemy. It did " + str(overall) + " damage"
        else:
            overall = comp1_Attacks[user][0]
            response = "- - PLAYER used "+ user + "on the enemy. It did " + str(overall) +" damage"
        print (response)
        fileopen("BOT1.yml", response)
        DMG_Effect(overall)
    if turn == 2:
        dec = random.randint(0, 2)
        if two_val[dec][1]== ENEM_Stat['WEAKNESS'][0]:
            overall = ENEM_Stat["WEAKNESS"][1] + two_val[dec][0]
            response = "- - COMP2 used " + str(two_key[dec]) + " on the enemy. It did " + str(overall) + " damage"
        else:
            overall = two_val[dec][0]
            response = "- - COMP2 used " + str(two_key[dec]) + " on the enemy. It did " + str(overall) + " damage"
        print(response)
        fileopen("BOT2.yml", response)
        DMG_Effect(overall)
        time.sleep(2)
    if turn == 3:
        dec = random.randint(0, 2)
        if three_val[dec][1]== ENEM_Stat['WEAKNESS'][0]:
            overall = ENEM_Stat["WEAKNESS"][1] + three_val[dec][0]
            response = "- - COMP3 used " + str(three_key[dec]) + " on the enemy. It did " + str(overall) + " damage"
        else:
            overall = three_val[dec][0]
            response = "- - COMP3 used " + str(three_key[dec]) + " on the enemy. It did " + str(overall) + " damage"
        print(response)
        fileopen("BOT3.yml", response)
        DMG_Effect(overall)
        time.sleep(2)
    if turn == 4:
        dec = random.randint(0, 2)
        if four_val[dec][1]== ENEM_Stat['WEAKNESS'][0]:
            overall = ENEM_Stat["WEAKNESS"][1] + four_val[dec][0]
            response = "- - COMP4 used " + str(four_key[dec]) + " on the enemy. It did " + str(overall) + " damage"
        else:
            overall = four_val[dec][0]
            response = "- - COMP4 used " + str(four_key[dec]) + " on the enemy. It did " + str(overall) + " damage"
        print(response)
        fileopen("BOT4.yml", response)
        DMG_Effect(overall)
        time.sleep(2)
    turn = turn +1
