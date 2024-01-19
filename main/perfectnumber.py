# Program to check whether a given number is perfect or not.

# A perfect number is a positive integer that is equal to the 
# sum of its positive divisors, excluding the number itself.

num = int(input("Enter the number: "))
sum = 0

for x in range(1, num):
    if (num % x == 0):
        sum = sum + x

if sum == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
