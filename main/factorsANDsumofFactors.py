# Python program to find the factors and the sum of factors of a positive number

num = int(input("Enter a positive number: "))
factorSum = 0

if num <= 0:
    print("Please enter a positive number.")
else:
    print("Factors:", end=" ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
            factorSum += i
            
    print("\nSum of factors:", factorSum)
