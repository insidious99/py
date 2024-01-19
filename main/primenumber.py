# Program to check whether a given number 
# is a prime number or not.

num = int(input("Enter the number: "))

if num > 1:
    for x in range(2, num):
        if (num % x) == 0:
            print(num, "is not a prime number.")
            break
        
        else:
            print(num, "is a prime number.")
            break

else:
    print(num, "is not a prime number.")
