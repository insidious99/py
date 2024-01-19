# Write a program that asks the user to enter a positive integer n 
# and prints a triangle pattern of numbers.

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = "")
    print()
