"""
Debug example: Game - Guess number
"""

def play(answer):
    """
    Play the game -- ask for input and compare
    :param answer:
    :return: how many steps does the user success
    """
    steps = 1
    user_answer = input("Please make a guess: ")  # get the initial guess from user
    while user_answer != answer:
        if user_answer > answer:
            # if the user's guess is larger than the answer
            print("You guessed %s, it is LARGER than the solution! Make another guess and good luck!" % user_answer)
        elif user_answer < answer:
            print("You guessed %s, it is SMALLER than the solution! Make another guess and good luck!" % user_answer)
        user_answer = input("Make another guess: ")

    return steps

if __name__ == "__main__":
    answer = input("Judge: Please give the solution to the game: ")
    print("Now it is time to start guessing!")
    steps = play(answer)
    print("You win in %s steps!!" % steps)







