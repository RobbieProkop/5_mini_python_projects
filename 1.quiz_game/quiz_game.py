

print('Welcome to the quiz!')

lives = 3

questionList = [
  {
    "qestion": "What's the capital of Russia? ",
    'answer' : 'moscow',
    'lecture': 'You should brush up on your geography'
  },
  {
    "qestion": 'What is the current world population (in billions)? ',
    'answer' : '8',
    'lecture': 'We reached 8 billion in 2022'
  },
  {
    "qestion": "Who was the first man to walk on the moon? ",
    'answer' : 'neil armstrong',
    'lecture': 'Mr. Armstrong said "This is one small step for a man, one giant leap for mankind" after stepping on the moon in July of 1969'
  },
  {
    "qestion": "What is the national sport of Canada? ",
    'answer' : 'lacrosse',
    'lecture': 'I bet you thought it was hockey!'
  },
  {
    "qestion": "Who discovered gravity (First and last name)? ",
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
  

def question(qStr, answer, lecture):
  q = input(qStr)
  if q.lower() != answer:
    print(f'Sorry, the correct answer was {answer}.')
    print(lecture)
    global lives
    lives -= 1
    check_lives()
  else:
    print('Correct!')
    print("Next Question: ")
    

print("Rules: Please write all of your answers in lowecase, otherwise they will be considered incorrect")
playing = input("Would you like to play? ")


if playing.lower() != "yes":
  print("Come back when you want to play")
  exit()


print("Let's play")

# first question
question("What's the capital of Russia? ", 'moscow', 'You should brush up on your geography')
  
#  2nd question
question("What is the current world population (in billions)? ", "8", 'We reached 8 billion in 2022')

