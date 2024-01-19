sum = 0

while True:
    num = int(input("Enter a positive number (or enter a negative number to stop): "))
    
    if num < 0:
        break
    else: 
        sum += num

print("Sum of positive numbers:", sum)
