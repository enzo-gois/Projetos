print('Loop com o break')

for x in range(1,11):
  if x > 5:
    break
  print(x)

print('\nLoop com o continue')

for i in range(1,11):
  if(i == 5):
    continue
  print(i)