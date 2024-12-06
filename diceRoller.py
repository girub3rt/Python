#Ulimate dice roller 2000

import random
import time

rolls = 0

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "n":
        if rolls == 0:
            print("You didn't even try! :/")
            break
        else:
            print(f"You rolled {rolls} times.")
            print("Thank you for playing!")
            break

    if choice == "y":
        try:
            many = int(input("How many times do you roll? "))
            for i in range(many):
                print(f"Roll {i + 1}: {random.randint(1, 6)}")
            rolls += 1
        except ValueError:
            print("Please enter a number.")
    else:
        print("Your dice fell to the floor. :(")
        print("Try again!")
        time.sleep(2)