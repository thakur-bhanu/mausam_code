from random import randint
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2 :
    print("Player Score: {Player_wins} and Computer Score: {Computer_wins}" )
    print("...rock...")
    print("...paper...")
    print("...scissors...")



# random_num = randiant(0, 2)
random_num = randint(0, 2)



player = input("(Enter Your Choice):" ).lower()

if (random_num == 0):
    computer = "rock"
elif (random_num == 1):
    computer = "paper"
else:
    computer = "scissors"
print(f"The computer plays:{computer}")
if player == computer:
    print("It's a tie!")
elif player == "rock":
if computer == "paper":
    print("Computer wins")
computer_wins +=1


else:
    print("Player wins!")
player_wins +=1
elif player == "paper"
if computer == "rock"
    print('Player wins!')
player_wins +=1
else:
    print("computer wins!")
computer_wins +=1
elif (player == "scissors")

if (computer == "rock")
    print("Computer Wins!")
computer_wins +=1
else:
    print("Player Wins!")
player_wins +=1

else:
    print("Enter a valid Move")