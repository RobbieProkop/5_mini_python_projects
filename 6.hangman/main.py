# for get API request
import requests

# for random word
import random

# uppercase string characters
import string

url = 'https://www.randomlists.com/data/words.json'

res = requests.get(url)

print(res.status_code)
if res: 
  print('Response OK')
else:
  print('Response Failed')
  
words = res.json()['data']
# print(words)

def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word: #checking to make sure word does not contain - or space
    word = random.choice(words)
  return word

def hangman():
  word = get_valid_word(words)
  word_letters = set(word) # letters in the word
  alphabet = set(string.ascii_uppercase)
  guessed_letters = set() # what the user has guessed

  # getting user input
  user_letter = input("Guess a letter: ").upper()
  if user_letter in alphabet - guessed_letters:
    guessed_letters.add(user_letter)
    if user_letter in word_letters:
      word_letters.remove(user_letter)
  elif user_letter in guessed_letters:
    print(f"You've already guessed {user_letter}")
  else:
    print("Invalid character")
    
    
hangman()

