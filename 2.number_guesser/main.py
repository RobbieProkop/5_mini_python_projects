import random


a = 1
b = 10


r = random.randint(a, b)

print('Welcome to the number guesser extravaganza!')

numOfGuess = 0

while True: 
  numOfGuess += 1
  guess = input(f"Guess a number between {a} and {b}: ")
  
  if guess.isdigit():
    guess = int(guess)

  else:
    print(f'Please type a number between {a} and {b} ')
    continue
  
  if guess == r:
    print("You got it in", numOfGuess -1, "guesses")
    break
  elif guess > r: 
    print(f'The number is less than {guess}')
  else:
    print(f'The number is greater than {guess}')

# Game Using A Function

# numOfGuess = 8
# guess= ""
# def guess_again():
#   global guess
#   global numOfGuess
#   guess = input(f"Guess a number between {a} and {b}: ")
  
#   if numOfGuess == 0:
#     print(f"You lose. The correct number was {r}")
#     quit() 
#   if not guess.isdigit():
#     print("Invalid entry")
#     guess_again()
#   guess = int(guess)
#   if guess <= a or guess >= b:
#     print(f"Please enter a number between {a} and {b}")
#     guess_again()
#   if guess > r:
#     print(f"the number is less than {guess}")
#     numOfGuess -= 1

#     guess_again()

#   if guess < r:
#     print(f"the number is greater than {guess}")
#     numOfGuess -= 1
    
#     guess_again()

#   if guess == r:
#     print(f'Congratulations! You guessed the number with {numOfGuess} guesses remaining')
#     quit()
  
# guess_again()

