# Power
- For this assignment, I started off with the template supplied in the requirements for this assignment.
  def print_graph(n):
  def get_power(x, n):
  for i in range(-8, 9):

- I then noticed that there was a lot of errors in it so I tried adding the print () function
  def print_graph(n):
  def get_power(x, n):
  for i in range(-8, 9):
  print()
- It still had errors so I decided to go through the class readme file for functions and I realized I didn't put a return for the second def function. So here's what I put this time.
def print_graph(n):
    def get_power(x, n):
        return x ** n
for i in range(-8, 9):
    print()
- This time it had no errors and was able to be tested, it gave me a gigantic block of space but no *, but I'm glad that it's now getting somewhere.
- Then I took something from the pyramid assignment from last week and added the print('*') on it
def print_graph(n):
    def get_power(x, n):
        return x ** n
for i in range(-8, 9):
    print('*', end='')
    print()
- It gave me this as a result
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
