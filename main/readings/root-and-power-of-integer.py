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
