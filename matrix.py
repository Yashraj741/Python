# Take inputs from the user
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))
n = int(input("Enter the value of n: "))

# Create the list of tuples
result = [(i, j, k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k!=n)]

# Print the result
print(result)
