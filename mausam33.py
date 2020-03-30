from random import randint

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:

    # print(f"Player Score: {player_wins} and Computer Score: {computer_wins}" )
    # [ ye line neeche lihni h taaki score input k baad aaye ]

    print("...rock...")
    print("...paper...")
    print("...scissors...")

    #random_num = randiant(0, 2)
    random_num = randint(0, 2)

    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"
    print(f"The computer plays:{computer}")

    player = input("(Enter Your Choice):" ).lower()

# 1. if both player and compyter are same :

    if player == computer:
        print("It's a tie!")


# 2. If player enters rock

    elif player == "rock":
        if computer == "paper":
            print("Computer wins")
            computer_wins +=1
        elif computer == 'scissors':
            print("Player wins!")
            player_wins +=1


# 3. If player enters paper

    elif player == "paper":
        if computer == "rock":
            print('Player wins!')
            player_wins +=1
        else:
            print("computer wins!")
        computer_wins +=1


# 4. If player enters scissors

    elif player == "scissors":
        if computer == "rock":
            print("Computer Wins!")
            computer_wins +=1
        else:
            print("Player Wins!")
            player_wins +=1



    else:
        print("Enter a valid Move")

    print(f"Player Score: {player_wins} and Computer Score: {computer_wins}" )