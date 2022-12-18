import requests

res = requests.get('https://www.randomlists.com/data/words.json')

print(res.status_code)
if res: 
  print('Response OK')
else:
  print('Response Failed')
  
print(res.text)

out