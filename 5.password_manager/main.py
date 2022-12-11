# DO not use this in real life

from cryptography.fernet import Fernet



'''
def write_key():
  key = Fernet.generate_key()
  with open('key.key', 'wb') as key_file:
    key_file.write(key)
'''
def load_key():
  file = open('key.key', 'rb')
  key = file.read()
  file.close()
  return key

key = load_key()
master = input("What is your master password? ")

def view():
  with open('passowrds.txt', 'r') as f:
    for line in f.readlines():
      # rstrip removes the line break
      data = line.rstrip()
      user, passw = data.split('|')
      print('User:', user, 'Password:', passw)

def add():
  name = input("account Name: ")
  password = input("Password: ")
  
  with open('passowrds.txt', 'a') as f:
    f.write(name + "|" + password + '\n')
    
    
    

while True:
  mode = input('Would you like to add a new password, or view an existing one? (Type "add", "view", or "Q") ').lower()
  if mode == 'q':
    quit()
  if mode == 'view':
    view()
  elif mode == 'add':
    add()
  else:
    print('invalid choice')
    continue