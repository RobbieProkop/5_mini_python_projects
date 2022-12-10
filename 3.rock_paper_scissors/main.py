import random

user_wins = 0
comp_wins = 0

options = ['rock', 'paper', 'scissors']
while True:
  user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
  
  if user_input == 'q':
    quit()
    
  if user_input not in options:
    print('Error: Please type Rock, Paper, or Scissors')
    continue
  r = random.randint(0, 2)
  
  comp_choice = options[r]

  print('computer choice:', comp_choice)  
  print('user choice: ', user_input)
  if user_input == comp_choice :
    print('Tie Game')
  elif user_input == 'rock' and comp_choice == "paper":
    comp_wins += 1
    print('You lose')
  elif user_input == 'paper' and comp_choice == "scissors":
    comp_wins += 1
    print('You lose')
  elif user_input == 'scissors' and comp_choice == "rock":
    comp_wins += 1
    print('You lose')
  else:
    user_wins += 1
    print('You won that round')
  
  print(f'current score: user: {user_wins} computer: {comp_wins}')
  
  # if user_input == options[r]:
  #   print("Congratulations, you win.")

  #   break
  
  
  # 0 = rock, 1 = paper, 2 = scissors
  
  
  
  
  