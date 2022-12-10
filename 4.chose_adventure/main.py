name = input("Type your name: ")

print(f'Welcome, {name}, to this adventure!')

q1 = input("You have reached a deadend. Choose to go either left or right. ").lower()

if q1 == "left":
  q2 = input("You found a space ship, are you against going in? ").lower()
  if q2 == 'no':
    print('You try to fly the space ship, but you crashed it and died')
    print('Game Over')
    quit()
  else:
    print("Wow, you aren't very adventurous. I'm ending this game now due to your lack of courage and adventurousness.")
    print('Game Over')    
    quit()
elif q1 == 'right':
  q2 = input("A pack of angry dogs came up from behind and bit your legs and arms. Type 'call for help' or 'hide in the abandoned house' ").lower()
  if q2 == "call for help":
    print('The help comes too slowly. You died waiting.')
    print('Game Over')
    quit()
  else: 
    print("A psychotic drug addict kills you and steals everything you have.")
    print('Game Over')
    quit()
else:
  print("Wrong choice. A meteor fell from the sky and squashed you.")
  quit()  