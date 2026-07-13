import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break

        if attempts == max_attempts:
            print(
                f"You have reached maximum attempts. Correct answer is {secret_number}. Please try again.")
            break


if __name__ == "__main__":
    play_game()
