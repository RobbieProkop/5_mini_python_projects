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
  return word.upper() # must be upper case to match the uppercase guesses

def hangman():
  word = get_valid_word(words)
  word_letters = set(word.upper()) # letters in the word
  alphabet = set(string.ascii_uppercase)
  guessed_letters = set() # what the user has guessed
  
  lives = 7

  # getting user input
  while len(word_letters) > 0 and lives > 0:
    # letters used
    print('You have guessed: ', ' '.join(guessed_letters))
    
    #  what correct letters have been guessed
    word_list = [letter if letter in guessed_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))
    user_letter = input("Guess a letter: ").upper()
    print()
    if user_letter in alphabet - guessed_letters:
      guessed_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives -= 1
        print(f'Wrong guess. You have {lives} lives remaining')
    elif user_letter in guessed_letters:
      print(f"You've already guessed {user_letter}")
    else:
      print("Invalid character")
      
  #  once word letters length is completed or lives are at 0
  if lives == 0:
    print(f"Game over. The word was: {word}")
  else: 
    print(f"Great job, you guessed the word, {word}!")
  
    
    
hangman()

