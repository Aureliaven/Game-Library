import random
import time

def play_numguess():
    print("Welcome to number guess!")
    try:
        f = open("./numberguess.txt")
        rand = int(f.readline().strip())
        range = int(f.readline().strip())
        guesses = int(f.readline())
        f.close()
        f = open("./numberguess.txt", "w")
        f.close()
        print("Continuing saved game state.")
    except ValueError:
        while True:
            try:
                range = int(input("Enter an upper limit:\n"))
            except ValueError:
                print("Please enter a valid number!")
                continue
            break
        rand = random.randrange(0, range)
        guesses = 0
    except FileNotFoundError:    
        while True:
            try:
                range = int(input("Enter an upper limit:\n"))
            except ValueError:
                print("Please enter a valid number!")
                continue
            break
        rand = random.randrange(0, range)
        guesses = 0
    while True:
        try:
            print(f"Number of attempted guesses: {guesses}")
            guess = input(f"Enter your guess between 0 and {str(range)} (q to quit)\n")
            if guess == "q":
                f = open("./numberguess.txt", "w")
                f.write(str(rand) + "\n")
                f.write(str(range) + "\n")
                f.write(str(guesses))
                f.close()
                print("Progress saved.")
                break    
            guess = int(guess)
            guesses += 1
            if guess == rand:
                print("You got it!")
                time.sleep(3)
                break
            else:
                print("Not quite.")
                if range > 10:
                    diff = abs(rand - guess)
                    if guesses >= 5 and diff > 25:
                        print("You're off by more than 25.")
                    elif guesses >= 4 and diff > 20:
                        print("You're off by more than 20.")
                    elif guesses >= 3 and diff > 15:
                        print("You're off by more than 15.")
                    elif guesses >= 2 and diff > 10:
                        print("You're off by more than 10.")
                    elif guesses >= 1 and diff > 5:
                        print("You're off by more than 5.")
                    else:
                        print("You're off by less than or equal to 5!")
                continue
        except ValueError:
            print("Enter a valid number!")
            continue    

# play_numguess()