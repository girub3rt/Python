#High Score -systeemi on vielä wonky.
#Pitäisi myös olla tarkistus minNum ja maxNum välillä.
#Ja jos viimeinen arvaus on oikein, pelin pitäisi päättyä onnistumiseen.

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

minNum = int(input("Enter a minimum number: "))
maxNum = int(input("Enter a maximum number: "))
guessAmount = int(input("Enter how many guesses: "))

numberGuess = random.randint(minNum, maxNum)

score = 0
hiScore = (get_highScore())

while True:
    try:
        guess = int(input(f"Guess a number between {minNum} and {maxNum}: "))
        if guessAmount == 0:
            print(f"You ran out of guesses. Correct answer is {numberGuess}")
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