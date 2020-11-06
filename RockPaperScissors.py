import random # imports random
from random import randint #imports randint
import time # imports ti
randomList = ["Rock", "Paper", "Scissors"]

playerScore = 0 # if playerScore goes up to 3 then player wins
comScore = 0 # if comScore goes up to 3 then computer wins
rounds = 0

# round 1
print("Rock, Paper, or Scissors? Computer: " + str(comScore) + " Player: " + str(playerScore))
playerChoice = input()
comChoice = random.choice(randomList)
if playerChoice == "Rock":
    if comChoice == "Paper":
        print("Computer Wins Round 1")
        comScore = comScore + 1
        rounds = rounds + 1
    elif comChoice == "Scissors":
        print("Player Wins Round 1")
        playerScore = playerScore + 1
    else:
        print("Tie! Both won round 1!")
        playerScore = playerScore + 1
        comScore = comScore + 1
elif playerChoice == "Paper":
     if comChoice == "Scissors":
         print("Computer Wins Round 1")
         comScore = comScore + 1
         rounds = rounds + 1
     elif comChoice == "Rock":
         print("Player Wins Round 1")
         playerScore = playerScore + 1
         rounds = rounds + 1
     else:
         print("Tie! Both won round 1!")
         playerScore = playerScore + 1
         comScore = comScore + 1
         rounds = rounds
elif playerChoice == "Scissors":
    if comChoice == "Rock":
         print("Computer Wins Round 1")
         comScore = comScore + 1
         rounds = rounds + 1
    elif comChoice == "Paper":
        print("Player Wins Round 1")
        playerScore = playerScore + 1
        rounds = rounds + 1
    else:
        print("Tie! Both won round 1! ")
        playerScore = playerScore + 1
        comScore = comScore + 1
        rounds = rounds
else:
    print("Your choice was invalid.")
    input()
    exit()

# round 2
print("Rock, Paper, or Scissors? Computer: " + str(comScore) + " Player: " + str(playerScore))
playerChoice = input()
comChoice = random.choice(randomList)
if playerChoice == "Rock":
    if comChoice == "Paper":
        print("Computer Wins Round 2")
        comScore = comScore + 1
        rounds = rounds + 1
    elif comChoice == "Scissors":
        print("Player Wins Round 2")
        playerScore = playerScore + 1
    else:
        print("Tie! No one won this round!")
        playerScore = playerScore + 1
        comScore = comScore + 1
elif playerChoice == "Paper":
     if comChoice == "Scissors":
         print("Computer Wins Round 2")
         comScore = comScore + 1
         rounds = rounds + 1
     elif comChoice == "Rock":
         print("Player Wins Round 2")
         playerScore = playerScore + 1
         rounds = rounds + 1
     else:
         print("Tie! No one won this round!")
elif playerChoice == "Scissors":
    if comChoice == "Rock":
         print("Computer Wins Round 2")
         comScore = comScore + 1
         rounds = rounds + 1
    elif comChoice == "Paper":
        print("Player Wins Round 2")
        playerScore = playerScore + 1
        rounds = rounds + 1
    else:
        print("Tie! Both won round 2! ")
        playerScore = playerScore + 1
        comScore = comScore + 1
        rounds = rounds
else:
    print("Your choice was invalid.")
    input()
    exit()

#round 3
print("Rock, Paper, or Scissors? Computer: " + str(comScore) + " Player: " + str(playerScore))
playerChoice = input()
comChoice = random.choice(randomList)
if playerChoice == "Rock":
    if comChoice == "Paper":
        print("Computer Wins Round 3")
        comScore = comScore + 1
        rounds = rounds + 1
    elif comChoice == "Scissors":
        print("Player Wins Round 3")
        playerScore = playerScore + 1
    else:
        print("Tie! No one won this round!")
        playerScore = playerScore + 1
        comScore = comScore + 1
elif playerChoice == "Paper":
     if comChoice == "Scissors":
         print("Computer Wins Round 3")
         comScore = comScore + 1
         rounds = rounds + 1
     elif comChoice == "Rock":
         print("Player Wins Round 3")
         playerScore = playerScore + 1
         rounds = rounds + 1
     else:
         print("Tie! No one won this round!")
elif playerChoice == "Scissors":
    if comChoice == "Rock":
         print("Computer Wins Round 3")
         comScore = comScore + 1
         rounds = rounds + 1
    elif comChoice == "Paper":
        print("Player Wins Round 3")
        playerScore = playerScore + 1
        rounds = rounds + 1
    else:
        print("Tie! Both won round 3! ")
        playerScore = playerScore + 1
        comScore = comScore + 1
        rounds = rounds
else:
    print("Your choice was invalid.")
    input()
    exit()

# time to show the results
print("=============================================")
time.sleep(2)
if playerScore > comScore:
    print("Player has won the game!")
    input()
    exit()
elif playerScore < comScore:
    print("Computer has won the game!")
    input()
    exit()
else:
    print("Tie! Both has won!")
    input()
    exit()



