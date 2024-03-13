stacks = int(input("How big do ya want this pyramid? "))
if stacks >= 9 or stacks == 0: 
   print ("\nNO!\n") 
elif stacks >= 1 and stacks <= 8: 
  for i in range(stacks, -1, -1):
    for j in range(stacks):
      if j >= i:
        print('#', end='')
    print()
  print("\nHere ya go mate :>")