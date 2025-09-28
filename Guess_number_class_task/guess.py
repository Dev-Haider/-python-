import random

while True:  
    random_number = random.randint(1, 10)
    print("Welcome to the guessing number game!")
    print("Guess a number between 1 and 10. You have 3 chances.")

    chances = 3  

    while chances > 0:
        guess = int(input("Enter your guess: "))

        if guess == random_number:
            print(" Excellent! Your guess is right.")
            break
        elif guess < random_number:
            print("Your guess is low, try again!")
        else:
            print("Your guess is too high, try again!")

        chances -= 1
        print(f"Chances left: {chances}")

    if chances == 0:
        print(f" Sorry, you're out of chances! The correct number was {random_number}.")

 
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        print("Goodbye! ")
        if play_again == "yes":
          print("lets play again ")
        break
