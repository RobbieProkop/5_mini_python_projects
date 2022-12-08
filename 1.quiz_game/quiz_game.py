import random

lives = 3

questionList = [
  {
    "question": "What's the capital of Russia? ",
    'answer' : 'moscow',
    'lecture': 'You should brush up on your geography'
  },
  {
    "question": 'What is the current world population (in billions)? ',
    'answer' : '8',
    'lecture': 'We reached 8 billion in 2022'
  },
  {
    "question": "Who was the first man to walk on the moon? ",
    'answer' : 'neil armstrong',
    'lecture': 'Mr. Armstrong said "This is one small step for a man, one giant leap for mankind" after stepping on the moon in July of 1969'
  },
  {
    "question": "What is the national sport of Canada? ", 
    'answer' : 'lacrosse',
    'lecture': 'I bet you thought it was hockey!'
  },
  {
    "question": "Who discovered gravity? ",
    'answer' : 'isaac newton',
    'lecture': 'Come on! Maybe you need to go back to elementary.'
  },
  {
    "question": "What is the worlds longest river called? ",
    'answer' : 'the nile',
    'lecture': 'The Nile is in Egypt.'
  },
  {
    "question": "Which country gifted the Statue of Liberty to the USA? ",
    'answer' : 'france',
    'lecture': 'France gave it as a congratulations for winning independance against Britain.'
  },
  {
    "question": "How many bones are there in the human body? ",
    'answer' : '206',
    'lecture': 'That\' a lot of bones.'
  },
]

def check_lives():
  if (lives != 0) and (lives > 1):
    print(f'You have {lives} lives remaining')
    print("Next Question: ")
    return print()
  if lives == 1:
    print(f'You have {lives} life remaining')
    print("Next Question: ")
    return print()
  
  print("You are out of lives. Game over!")
  exit()

def random_question():
  currentDict = random.choice(questionList)
  qStr = currentDict['question']
  answer = currentDict['answer']
  lecture =  currentDict['lecture']
  return [qStr, answer, lecture]

def question():
  current = random_question()
  q = input(current[0])
  if q.lower() != current[1]:
    print(f'Sorry, the correct answer was {current[1]}.')
    print()
    print(current[2])
    print()
    global lives
    lives -= 1
    check_lives()
  else:
    print('Correct!')
    print("Next Question: ") 
    print()


print('Welcome to the quiz!')
print()

print("Rules: Please write all of your answers in lowecase, otherwise they will be considered incorrect")
print()

print("You must go through 10 questions, with no more than 3 wrong answers to win! If the question asks for the name of a person, please enter the fist and last name")
print()

playing = input("Are you ready to start? ")
print()

if playing.lower() != "yes":
  print("Come back when you want to play")
  exit()

print("Let's play")

print()


# 1st question
question()
  
#  2nd question
question()

# 3rd question
question()
  
#  4th question
question()

print(f"Congratulation, you won the game with {lives} lives remaining!")
