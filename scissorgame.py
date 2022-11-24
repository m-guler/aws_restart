import random
howmany = input("how many times you want to play")
x = int(howmany)
i = 1
cpu_win = 0
player_win = 0

for i in range(x):


 choices = ["rock","paper","scissors"]

 cpuchoice = random.choice(choices)

 mychoice = input("choose rock paper or scissors")



 if mychoice == cpuchoice:
    print("we choose the same")

 elif mychoice == "rock":
    if cpuchoice == "scissors":
     print("I choose", cpuchoice )
     print("you choose", mychoice )
     print("you win")
     player_win = player_win + 1
 
    if cpuchoice == "paper":
     print("I choose", cpuchoice )
     print("you choose", mychoice )
     print("you lost") 
     cpu_win = cpu_win + 1
 

 elif mychoice == "paper":
    if cpuchoice == "rock":
     print("I choose", cpuchoice )
     print("you choose", mychoice )
     print("you win")
     player_win = player_win + 1
 
    if cpuchoice == "scissors":
     print("I choose", cpuchoice )
     print("you choose", mychoice )
     print("you lost")
     cpu_win = cpu_win + 1
 

 elif mychoice == "scissors":
    if cpuchoice == "paper":
     print("I choose", cpuchoice )
     print("you choose", mychoice )
     print("you win")
     player_win = player_win + 1

    if cpuchoice == "rock":
     print("I choose", cpuchoice )
     print("you choose", mychoice )
     print("you lost")
     cpu_win = cpu_win + 1 
 
print("Cpu: ", cpu_win, "Your win :", player_win)
if cpu_win > player_win:
 print("you are loser")
elif cpu_win < player_win:
 print("you are the winner")
elif cpu_win == player_win: 
 print("no one wins")



