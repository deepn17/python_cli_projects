import random

num_to_guess = random.randint(1, 100)

counter = 0

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("Please enter whole numbers only.")
        continue

    counter = counter + 1

    if guess > num_to_guess:
        print("Your guess is too high.")
    elif guess < num_to_guess:
        print("Your guess is too low.")
    else:
        print(f"You have guessed it correct in {counter} attempts.")
        break








