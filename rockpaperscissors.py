import random
import time

rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
    "exit": "exit"
}

modes = ["1", "2", "singleplayer", "multiplayer"]

def play_rps():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        mode = str(input("Singleplayer (1) or multiplayer (2)?\n"))
        if mode not in modes:
            print("Enter a valid mode!")
            continue
        else:
            break
    if mode == "1" or mode == "singleplayer":
        singleplayer()
    elif mode == "2" or mode == "multiplayer":
        multiplayer()
    else:
        print("Something went wrong :/")
    time.sleep(3)

def singleplayer():
    pscore = 0
    cscore = 0
    num_rounds = 0
    while True:
        while True:
            p_move = str(input("What's your move? (Rock, paper, scissors, or exit)\n")).lower()
            if p_move not in rules.keys():
                print("Invalid move!\n")
                continue
            else:
                break
        c_move = random.choice(["rock","paper","scissors"])
        if p_move == "exit":
            print("\nThanks for playing!")
            print("Summary:")
            print("Rounds played: " + str(num_rounds))
            print("You won " + str(pscore) + " rounds.")
            print("Computer won " + str(cscore) + " rounds.")
            break
        elif p_move == c_move:
            print("It's a tie\n")
            num_rounds += 1
            continue
        elif rules[p_move] == c_move:
            print("You won this round!\n")
            num_rounds += 1
            pscore += 1
            continue
        elif rules[c_move] == p_move:
            print("Computer wins this round!\n")
            num_rounds += 1
            cscore += 1
            continue
        else:
            print("Something went wrong :/")
            break

def multiplayer():
    while True:
        p1_name = input("Enter player 1's name:\n")
        p2_name = input("Enter player 2's name:\n")
        if not p1_name or not p2_name:
            print("You did not enter a player's name!")
            continue
        else:
            break
    p1_score = 0
    p2_score = 0
    num_rounds = 0
    while True:
        while True:
            p1_move = str(input("Player 1, what's your move? (Rock, paper, scissors, or exit)\n")).lower()
            if p1_move not in rules.keys():
                print(p1_name + " made an invalid move!\n")
                continue
            p2_move = str(input("Player 2, what's your move? (Rock, paper, scissors, or exit)\n")).lower()
            if p2_move not in rules.keys():
                print(p2_name + " made an invalid move!\n")
                continue
            else:
                break
        if p1_move == "exit" or p2_move == "exit":
            print("\nThanks for playing!")
            print("Summary:")
            print("Rounds played: " + str(num_rounds))
            print(p1_name + " won " + str(p1_score) + " rounds.")
            print(p2_name + " won " + str(p2_score) + " rounds.")
            break
        elif p1_move == p2_move:
            print("It's a tie\n")
            num_rounds += 1
            continue
        elif rules[p1_move] == p2_move:
            print(p1_name + " wins this round!\n")
            num_rounds += 1
            p1_score += 1
            continue
        elif rules[p2_move] == p1_move:
            print(p2_name + " wins this round!\n")
            num_rounds += 1
            p2_score += 1
            continue
        else:
            print("Something went wrong :/")
            break

# play_rps()