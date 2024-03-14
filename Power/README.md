# Power
- For this assignment, I started off with the template supplied in the requirements for this assignment.
''' python
  def print_graph(n):
  def get_power(x, n):
  for i in range(-8, 9):
'''

- I then noticed that there was a lot of errors in it so I tried adding the print () function
''' python
  def print_graph(n):
  def get_power(x, n):
  for i in range(-8, 9):
  print()
'''
- It still had errors so I decided to go through the class readme file for functions and I realized I didn't put a return for the second def function. So here's what I put this time.
'''python
def print_graph(n):
    def get_power(x, n):
        return x ** n
for i in range(-8, 9):
    print()
'''
- This time it had no errors and was able to be tested, it gave me a gigantic block of space but no *, but I'm glad that it's now getting somewhere.
- Then I took something from the pyramid assignment from last week and added the print('*') on it
def print_graph(n):
    def get_power(x, n):
        return x ** n
for i in range(-8, 9):
    print('*', end='')
    print()
- It gave me this as a result
'''
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
'''
- I then tried to change the equation from x ** n to x * x but I wasn't getting anything other than the previous result.
- So I tried adding an X axis to it by also taking the "for j in range(0, 9):" my previous assignment and I got the following
'''
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
*********
'''
- Then I tried indenting the for functions to see if it'll do anything but as a result, it shows me nothing.
- I tried moving the range to the top but it just gave me a long string of '*'
'''
*********************************************************************************************************************************************************%
'''    
-
