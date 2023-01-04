# Get integer from user
n = int(input("Enter an integer: "))

# Initialize variables
root = 0
pwr = 0

# Try all values of root and pwr
for i in range(1, 6):
  for j in range(1, 6):
    if i**j == n:
      root = i
      pwr = j
      break

# Print result
if root == 0 and pwr == 0:
  print("No such pair of integers exists.")
else:
  print("root =", root)
  print("pwr =", pwr)

#This program first gets an integer from the user using the input() function. It then initializes the variables root and pwr to 0.
#The program then uses two nested for loops to try all possible values of root and pwr in the range 1 to 5. 
#For each pair of values, it checks if root**pwr is equal to the integer entered by the user. 
#If it is, it sets root and pwr to the values that satisfy the condition and breaks out of the loops.
#Finally, the program checks if root and pwr are still equal to 0. 
#If they are, it means that no such pair of integers was found, and it prints a message to that effect.
#If root and pwr have been set to non-zero values, it means that a pair of integers was found, and it prints the values of root and pwr.