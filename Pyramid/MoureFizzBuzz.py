for index in range(1, 100, 1):
  if index % 3 == 0 and index % 5 == 0:
    print ('fizz' + 'buzz')
  elif index % 3 == 0:
      print('fizz')
  elif index % 5 == 0:
      print('buzz')  
  else:
    print(index)
