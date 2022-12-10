# DO not use this in real life

master = input("What is your master password? ")

mode = input('Would you like to add a new password, or view an existing one? (Type "add", "view", or "Q") ').lower()

while True:
  if mode == 'q':
    quit()
  if mode == 'view':
    pass
  elif mode == 'add':
    pass
  else:
    print('invalid choice')
    continue