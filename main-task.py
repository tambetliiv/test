import re

file = open("input.txt", "r")

for line in file:
  ip = line.strip()
  pref_port = int(re.split('/|:', ip)[1])
  if pref_port % 3 == 0 and pref_port % 5 == 0:
    print('fizzbuzz')
  elif pref_port % 3 == 0:
    print('fizz')
  elif pref_port % 5 == 0:
    print('buzz')
  else:
    print(pref_port)

file.close()


