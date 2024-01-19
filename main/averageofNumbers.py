sum = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    
    if num == 0:
        break
    else:
        sum += num
        count += 1

if count == 0:
    print("No numbers were entered.")
else:
    avg = sum / count
    print("Average of entered numbers:", avg)
