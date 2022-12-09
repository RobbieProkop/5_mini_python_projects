import random


a = 1
b = 10

r = random.randint(a, b)

guess= ""

def guess_again():
  global guess
  guess = input(f"Guess a number between {a} and {b}: ")
  if int(guess) > r:
    print(f"the number is less than {guess}")
    guess_again()

  if int(guess) < r:
    print(f"the number is greater than {guess}")
    guess_again()

  if int(guess) == r:
    return
  

# guess = input(f"Guess a number between {a} and {b}: ")
guess_again()
print('Congratulations! You win!')
