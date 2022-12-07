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
    "question": "Who discovered gravity (First and last name)? ",
    'answer' : 'isaac newton',
    'lecture': 'Come on! Maybe you need to go back to elementary.'
  },
]

def check_lives():
  if lives != 0:
    print(f'You have {lives} remaining')
    return print("Next Question: ")
  
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
    print(current[2])
    global lives
    lives -= 1
    check_lives()
  else:
    print('Correct!')
    print("Next Question: ") 


print('Welcome to the quiz!')

print()

print("Rules: Please write all of your answers in lowecase, otherwise they will be considered incorrect")

print()

playing = input("Would you like to play? ")

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

print("Congratulation, you won the game!")
