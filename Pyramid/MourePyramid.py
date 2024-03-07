stacks = int(input("How big do ya want this pyramid? "))
if stacks == 0 or stacks >= 9: 
   print ("\nNO!\n") 
   stacks = int(input("How big do ya want this pyramid? "))
   if stacks == 0 or stacks >= 9: 
    print ("\nYou get ONE more try\n") 
    stacks = int(input("How big do ya want this pyramid? "))
    if stacks == 0 or stacks >= 9: 
      print ("\nGo kick some rocks mate :<\n")
      
elif stacks >= 1 and stacks <= 8: 
  for i in range(stacks, -1, -1):
    for j in range(stacks):
      if j >= i:
        print('#', end='')
    print()
  print("\nHere ya go mate :>")