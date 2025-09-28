# 🎮 Guessing Number Game (Python)

A simple **Python guessing game** where the player has **3 chances** to guess the correct number between 1 and 10. After the game ends, the player can choose to **play again** or **exit**.

---

## 📌 Features

* Random number generated between **1–10**.
* Player gets **3 chances** to guess.
* Game gives hints if the guess is too **high** or **low**.
* If chances finish, the correct number is revealed.
* Option to **play again** (`yes`) or **quit** (`no`).

---

## 🖥️ Code Example

```python
import random

while True:  
    random_number = random.randint(1, 10)
    print("Welcome to the guessing number game!")
    print("Guess a number between 1 and 10. You have 3 chances.")

    chances = 3  

    while chances > 0:
        guess = int(input("Enter your guess: "))

        if guess == random_number:
            print("🎉 Excellent! Your guess is right.")
            break
        elif guess < random_number:
            print("Your guess is low, try again!")
        else:
            print("Your guess is too high, try again!")

        chances -= 1
        print(f"Chances left: {chances}")

    if chances == 0:
        print(f"😢 Sorry, you're out of chances! The correct number was {random_number}.")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        print("Goodbye! 👋")
        break
    elif play_again == "yes":
        print("Let's play again! 🎮")
```

---

## ▶️ How to Run

1. Save the file as `guess_game.py`.
2. Open terminal/cmd and run:

   ```bash
   python guess_game.py
   ```
3. Follow on-screen instructions.

---

## 📚 Example Gameplay

```
Welcome to the guessing number game!
Guess a number between 1 and 10. You have 3 chances.
Enter your guess: 5
Your guess is low, try again!
Chances left: 2
Enter your guess: 8
🎉 Excellent! Your guess is right.
Do you want to play again? (yes/no): yes
Let's play again! 🎮
```

---

## 🏆 Learning Concepts

* Random number generation (`random.randint()`)
* Loops (`while`)
* Conditional statements (`if`, `elif`, `else`)
* User input handling (`input()`)

---

✨ This project is perfect for **beginners** learning Python basics!
