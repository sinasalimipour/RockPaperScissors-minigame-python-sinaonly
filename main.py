import random




# v.1


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

useroptions=['paper','rock','scissors']
uesrchoice =input("wellcome to Rock, Paper, Scissors  game enter your choice ");

if 'paper' in useroptions:
    if 'rock' in useroptions:
        if 'scissors' in useroptions:
          (print("you picked :" + "scissors"))
    (print("you picked :" + "rock"))
print("you picked :" + "paper")











