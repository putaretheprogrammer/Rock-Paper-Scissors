import random # imports random
from random import randint # imports randint
import time # imports time
rounds = 0
playerScore = 0
comScore = 0

def CallRound():
    global playerScore # if playerScore goes up to 3 then player wins
    global comScore # if comScore goes up to 3 then computer wins
    global rounds

    randomList = ["Rock", "Paper", "Scissors"]
        
    
    # round
    if rounds == 0:
        rounds = rounds + 1
        print("Round " + str(rounds))
    else:
        print("Round " + str(rounds))
        
    print("Rock, Paper, or Scissors? Computer: " + str(comScore) + " Player: " + str(playerScore))
    playerChoice = input()
    comChoice = random.choice(randomList)
    if playerChoice == "Rock":
        if comChoice == "Paper":
            print("Computer Wins Round " + str(rounds))
            comScore = comScore + 1
            rounds = rounds + 1
        elif comChoice == "Scissors":
            print("Player Wins Round " + str(rounds))
            playerScore = playerScore + 1
            rounds = rounds + 1
        else:
            print("Tie! Both won round 1!")
            playerScore = playerScore + 1
            comScore = comScore + 1
            rounds = rounds + 1
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
             rounds = rounds + 1
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
            rounds = rounds + 1
    else:
        print("Your choice was invalid.")
        input()
        exit()

print("How many rounds?")
roundCount = int(input())

for i in range(roundCount):
    CallRound()
    while playerScore == 3 or (playerScore > comScore and rounds == 3):
        print("Player wins!")
        input()
        exit()
    while comScore == 3 or comScore == 3 and rounds == 3:
        print("Computer wins!")
        input()
        exit()
    
