from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

def main():
    seed = int(input("Enter a seed number:\n"))
    seed_secret_numbers(seed)

    secret = generate_secret_number()
    attempts = 0
    correct = False

    while not correct:
        guess = int(input("What is your guess:\n"))
        attempts += 1

        message, correct = input_response(secret, guess)
        print(message)

    print(f"It took you {attempts} tries!")

if __name__ == "__main__":
    main()