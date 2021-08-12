# v.1

import random

# if list contains user choices:
#     print("you picked " + {input()} )
# uesrchoice =input("wellcome to Rock, Paper, Scissors  game enter your choice ");
#
# rook = "rook"
# paper = "paper"
# scissors = "scissors"
#
# if (uesrchoice==rook):
#    print("you pick rook")
# elif (uesrchoice==paper):
#     print("you pick paper")
# elif (uesrchoice==scissors):
#     print("you pick scissors")
# else:print("you did not pick the correct")
#
# # pcchoice
# #0 = rook
# #1 = paper
# #2 = scissors
#
#
# pcchoice = random.randint(0, 2);
# if (pcchoice==0):
#     print("i picked rook")
# elif (pcchoice==1):
#     print("i picked paper")
# else:print("i picked scissors")
#
#
#
#
# # draw section
# if (pcchoice==0  and uesrchoice==rook ):
#     print("draw")
# elif (pcchoice == 1 and uesrchoice==paper ):
#     print("draw")
# elif (pcchoice == 2 and uesrchoice==scissors):
#     print("draw")
# # draw  section
# ###
# ###
# # i won section
# elif (pcchoice == 0 and uesrchoice == scissors):
#     print("i won")
# elif (pcchoice == 1 and uesrchoice==rook ):
#     print("i won")
# elif (pcchoice == 2 and uesrchoice==paper ):
#     print("i won")
# # i won section
# ###
# ###
# # you won section
# elif (pcchoice == 1 and uesrchoice==scissors ):
#     print("you won")
# elif (pcchoice == 2 and uesrchoice == rook):
#     print("you won")
# elif (pcchoice == 0 and uesrchoice == paper):
#     print("you won")
# # you won section


# v.2


#listOfStrings = ['Hi' , 'hello', 'at', 'this', 'there', 'from']
#
# if 'at' in listOfStrings :
#     print("Yes, 'at' found in List : " , listOfStrings)


#
# import random, os, sys
# computerscore = 0
# userscore = 0
# numgames = int(input("Welcome to rock, paper, scissors.\nHow many games would you like to play?\n"))
# userinput = ""
# computerchoice = ""
# userwin = False
# draw = False
# choice = ""
# clear = lambda: os.system("cls")
#
# for x in range(0, numgames):
#     generatednum = random.randint(1,3)
#     if generatednum == 1:
#         computerchoice = "rock"
#     elif generatednum == 2:
#         computerchoice = "paper"
#     elif generatednum == 3:
#         computerchoice = "scissors"
#
#     userinput = input("Select rock, paper, or scissors\n")
#
#     if userinput == "rock" and computerchoice == "scissors":
#         print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
#         userscore += 1
#     elif userinput == "rock" and computerchoice == "paper":
#         print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
#         computerscore += 1
#     if userinput == "paper" and computerchoice == "rock":
#         print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
#         userscore += 1
#     elif userinput == "paper" and computerchoice == "scissors":
#         print("You selected",userinput,"and the computer selected",computerchoice,". You lost this round!")
#         computerscore += 1
#     if userinput == "scissors" and computerchoice == "paper":
#         print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
#         userscore += 1
#     elif userinput == "scissors" and computerchoice == "rock":
#         print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
#         computerscore += 1
#
# if userscore > computerscore:
#     userwin = True
# elif userscore == computerscore:
#     draw = True
#
# if userwin == True:
#     print("Congratulations, you won!\nYour score:",userscore,"\nComputer's score:",computerscore)
# elif draw == True:
#     print("You drew!\nYour score:",userscore,"\nComputer's score:",computerscore)
# elif userwin == False:
#     print("I'm sorry, but you lost.\nYour score:",userscore,"\nComputer's score:",computerscore)
#
# choice = str(input("Would you like to play again? y/n\n"))
# if choice == "y":
#     clear()
#     os.system("rockpaperscissors.py")


# v.3


# import random
#
# CHOICES = 'rps'
#
#
# def get_player_choice():
#     """Get user input and validate it is one of the choices above"""
#     player_choice = None
#     while player_choice is None:
#         player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
#         if player_choice.lower() not in CHOICES:
#             player_choice = None
#     return player_choice.lower()
#
#
# def get_computer_choice():
#     """Have the computer pick one of the valid choices at random"""
#     computer_choice = random.randint(0, 2)
#     computer_choice = CHOICES[computer_choice]
#     return computer_choice
#
#
# def is_draw(player_choice, computer_choice):
#     """Check if game was a draw"""
#     if player_choice == computer_choice:
#         return True
#
#
# def print_winner(player_choice, computer_choice):
#     """Check to see who won"""
#     if player_choice == 'r' and computer_choice == 's':
#         print('Player wins!')
#     elif player_choice == 's' and computer_choice == 'p':
#         print('Player wins!')
#     elif player_choice == 'p' and computer_choice == 'r':
#         print('Player wins!')
#     else:
#         print('Computer wins!')
#         print('%s beats %s' % (computer_choice, player_choice))
#
#
# def play_game():
#     """play the game"""
#     player_choice = get_player_choice()
#     computer_choice = get_computer_choice()
#     if is_draw(player_choice, computer_choice):
#         print("It's a draw, both players picked %s: " % player_choice)
#     else:
#         print("Computer picked: %s" % computer_choice)
#         print("Player picked: %s" % player_choice)
#         print_winner(player_choice, computer_choice)
#
#
# if __name__ == "__main__":
#     play_game()
#

# v.4
