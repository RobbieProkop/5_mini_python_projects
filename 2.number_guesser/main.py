import random


a = 1
b = 100

r = random.randint(a, b)

numOfGuess = 0

guess= ""

def guess_again():
  global guess
  global numOfGuess
  guess = input(f"Guess a number between {a} and {b}: ")
  
  if not guess.isdigit():
    print("Invalid entry")
    guess_again()
  guess = int(guess)
  if guess <= a or guess >= b:
    print(f"Please enter a number between {a} and {b}")
    guess_again()
  if guess > r:
    print(f"the number is less than {guess}")
    numOfGuess += 1
    print("first ",numOfGuess)
    guess_again()

  if guess < r:
    print(f"the number is greater than {guess}")
    numOfGuess += 1
    print("second ",numOfGuess)
    guess_again()

  if guess == r:
    numOfGuess += 1
    print(f'Congratulations! You guessed the number with {numOfGuess} guesses')
    quit()
  
guess_again()

