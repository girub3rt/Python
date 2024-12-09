#High Score -systeemi on vielä wonky.
#Jos vaikeustaso, eli minNum ja maxNum välinen arvo on alle 10, ei oteta hiScorea

import random

def get_highScore() -> int:
    filename = "numberGuesserScore.txt"
    with open(filename, "r") as file:
        val = file.read()
        if val == "":
            highScore = 0
        else:
            highScore = int(val)
    return highScore

def set_score(highScore) -> None:
    with open("numberGuesserScore.txt", "w") as file:
        file.write(str(highScore))


score = 0
hiScore = (get_highScore())

while True:
    try:
        minNum = int(input("Enter a minimum number: "))
        maxNum = int(input("Enter a maximum number: "))
        if minNum > maxNum:
            print("Minimum number is greater than maximum number.")
        else:
            break
    except ValueError:
        print("Please enter a number.")

guessAmount = int(input("Enter how many guesses: "))
guessAmount -= 1

numberGuess = random.randint(minNum, maxNum)

while True:
    try:
        guess = int(input(f"Guess a number between {minNum} and {maxNum}: "))
        if guessAmount == 0:
            if guess == numberGuess:
                print("Good job, you guessed it on the last try!")
                print(f"Your score is {score}!")
                if score < int(hiScore):
                    hiScore = score
                    set_score(hiScore)
                print(f"Current highscore is {hiScore}.")
                break
            else:
                print(f"You ran out of guesses. Correct answer is {numberGuess}")
                print(f"Current highscore is {hiScore}.")
                break
        if guess < minNum or guess > maxNum:
            print("Out of range. Try again.")
        elif guess < numberGuess:
            guessAmount -= 1
            score += 1
            print("Too low. Try again.")
        elif guess > numberGuess:
            guessAmount -= 1
            score += 1
            print("Too high. Try again.")
        else:
            score += 1
            print("Correct!")
            print(f"Your score is {score}!")
            if score < int(hiScore):
                hiScore = score
                set_score(hiScore)
            print(f"Current highscore is {hiScore}.")
            break
    except ValueError:
        print("Please enter a number.")