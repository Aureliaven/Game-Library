from connect4 import play_c4
from tictactoe import play_t3
from rockpaperscissors import play_rps
from numberguess import play_numguess
from hangman import play_hangman

game_lib = {
    1: "Connect Four",
    2: "Tic-Tac-Toe",
    3: "Rock, Paper, Scissors",
    4: "Number Guessing",
    5: "Hangman"
}
while True:
    print("""
Your game library:
1: Connect Four
2: Tic-Tac-Toe
3: Rock, Paper, Scissors
4: Number Guessing
5: Hangman
""")
    game_choice = input("""
What game would you like to play?
Input the game ID, or type 'exit' to exit.
""")

    if game_choice == '1':
        play_c4()
        game_choice = None

    elif game_choice == '2':
        play_t3()
        game_choice = None

    elif game_choice == '3':
        play_rps()
        game_choice = None

    elif game_choice == '4':
        play_numguess()
        game_choice = None
    
    elif game_choice == '5':
        play_hangman()
        game_choice = None

    elif game_choice == 'exit':
        break