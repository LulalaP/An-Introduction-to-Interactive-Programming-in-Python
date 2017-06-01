# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    else:
        return 4


def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    else:
        return "scissors"
    

def rpsls(player_choice): 
    print "Player chooses",player_choice   
    player_num=name_to_number(player_choice)
    computer_num=random.randrange(0,5)
    computer_choice=number_to_name(computer_num) 
    print "Computer chooses",computer_choice
    remainder=(computer_num-player_num)%5
    if (remainder==1) or (remainder==2):
        print "Computer wins!\n"
    elif (remainder==3) or (remainder==4):
        print "Player wins!\n"
    else:
        print "Player and computer tie!\n"
    

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
