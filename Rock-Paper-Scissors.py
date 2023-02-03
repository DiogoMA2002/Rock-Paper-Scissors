import random

hand = ["rock", "paper", "scissors"]

computer = hand[random.randint(0,2)]

player = False

scoreComputer=0
scorePlayer=0

exit = ""
while player == False:
     player = input("Rock, Paper, Scissors > ")
     if player.upper() == computer.upper():
          print("Tie!")
          scoreComputer+=1
          scorePlayer+=1
     elif player.upper() == "ROCK":
          if computer.upper() == "PAPER":
               print("Computer Wins")
               scoreComputer+=1
               player = False
          else:
               print("Computer loses")
               scorePlayer+=1
     elif player.upper() == "PAPER":
          if computer.upper() == "SCISSORS":
               print("Computer Wins")
               scoreComputer+=1
               player = False
          else:
               print("Computer loses")
               scorePlayer+=1
     elif player.upper() == "SCISSORS":
          if computer.upper() == "ROCK":
               print("Computer Wins")
               scoreComputer+=1
               player = False
          else:
               print("Computer loses")
               scorePlayer+=1
     else:
          print("Invalid play, please try again")
     exit = input("Stop? (yes or no) > ")
     if exit.upper() == "YES":
          print(f"Computer Score: {scoreComputer}\n Player Score: {scorePlayer}")
          break
     player = False
     computer = hand[random.randint(0,2)]
     


