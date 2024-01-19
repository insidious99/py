min = 99999
max = 0
choice = "y"

while choice == "y" or choice == "Y":
    num = int(input("Enter a number: "))
    if num > max:
        max = num
    if num < min:
        min = num
    choice = input("Do you wish to continue (y/n)?: ")

print("Maximum number:", max)
print("Minimum number:", min)
