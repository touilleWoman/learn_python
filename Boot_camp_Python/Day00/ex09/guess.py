import random

def ask():
    return input("What's your guess between 1 and 99?\n")


def start_game():
    right_nb = random.randint(1, 99)
    print("This is an interactive guessing game!\n"
        "You have to enter a number between 1 and 99 to "
        "find out the secret number.\n"
        "Type 'exit' to end the game.\nGook luck!"
        )
    count = 0
    guess = ask()
    while guess != "exit" and guess != str(right_nb):
        if not guess.isdigit():
            print("That's not a number.")
        elif int(guess) > right_nb:
            print("Too high!")
        elif int(guess) < right_nb:
            print("Too low!")
        guess = ask()
        count += 1
    if guess == str(right_nb):
        if right_nb == 42:
            print("The answer to the ultimate question of life,"
            " the universe and everything is 42")
        if count == 0:
            print("Congratulations! You got it on your first try!")
        else:
             print("Congratulations, you've got it!\n"
                "You won in {} attempts!".format(count + 1))
    elif guess == "exit":
        print("Goodbye!")


if __name__ == '__main__':
    start_game()