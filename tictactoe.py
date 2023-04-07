import random
import time
import io

BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}


def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    global BOARD
    print(f"""
         {BOARD[1]} | {BOARD[2]} | {BOARD[3]}
        ---+---+---
         {BOARD[4]} | {BOARD[5]} | {BOARD[6]}
        ---+---+---
         {BOARD[7]} | {BOARD[8]} | {BOARD[9]}
        """)


def get_action(player, game_round):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    while True:
        try:
            action = input(f"Player {player}, choose a board space (1-9, q to quit).\n")
            if action == 'q':
                f = open("./tictactoe.txt", "w")
                f.write(player)
                f.write(str(game_round))
                for space in BOARD.values():
                    f.write(space)
                f.close()
                print("Progress saved.")
                time.sleep(2)
                return action
            action = int(action)
            if action not in range(1,10):
                print("Please enter a valid board space (1-9).\n")
                continue
            return action
        except ValueError:
            print("Please enter a valid board space (1-9).\n")
            continue
        break


def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    print(f"Congrats Player {player}, you win!\n")
    render()
    time.sleep(3)

def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    global BOARD
    if BOARD[1] == player:
        if BOARD[2] == player and BOARD[3] == player:
            victory_message(player)
            return True
        elif BOARD[4] == player and BOARD[7] == player:
            victory_message(player)
            return True
        elif BOARD[5] == player and BOARD[9] == player:
            victory_message(player)
            return True
    elif BOARD[2] == player and BOARD[5] == player and BOARD[8] == player:
            victory_message(player)
            return True
    elif BOARD[3] == player:
        if BOARD[6] == player and BOARD[9] == player:
            victory_message(player)
            return True
        elif BOARD[5] == player and BOARD[7] == player:
            victory_message(player)
            return True
    elif BOARD[4] == player and BOARD[5] == player and BOARD[6] == player:
        victory_message(player)
        return True
    elif BOARD[7] == player and BOARD[8] == player and BOARD[9] == player:
        victory_message(player)
        return True
    return False

def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''
    global BOARD
    try:
        f = open("./tictactoe.txt")
        player = f.read(1)
        game_round = int(f.read(1))
        for i in range(1,10):
            BOARD[i] = f.read(1)
        f.close()
        f = open("./tictactoe.txt", "w")
        f.close()
        print("Continuing saved game state.")
    except io.UnsupportedOperation:
        player = random.choice(['X', 'O'])
        game_round = 0
    except FileNotFoundError:
        player = random.choice(['X', 'O'])
        game_round = 0

    game_over = False
    while not game_over:

        # Print the current state of the board
        render()

        # Get the current player's action and assign it to a variable called 'action'.
        action = get_action(player, game_round)
        if action == "q":
            break

        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.
        BOARD[action] = player

        # Increment the game round by 1.
        game_round += 1

        # Check if the game is winnable (game_round >= 4),
            # then check for win conditions (check_win(player)),
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).
        if game_round >= 5:
            if check_win(player):
                game_over = True


        # Check if there are any open spots left (game_round == 9),
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.
        if game_round == 9:
            print("It's a tie!\n")
            game_over = True

        # switch players with a quick conditional loop.
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop
            
        # and reinitiate the game loop (play_t3()).
    while True:
        again = str(input("Play again? (y/n)\n"))
        if again != 'y' and again != 'n':
            print("Enter a valid response\n")
            continue
        if again == 'y':
            BOARD = {1: ' ',  2: ' ',  3: ' ',
                         
                     4: ' ',  5: ' ',  6: ' ',

                     7: ' ',  8: ' ',  9: ' '}
            play_t3()
            break
        else:
            break