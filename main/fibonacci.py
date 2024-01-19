n = int(input("Enter number of terms: "))

first = third = 0
second = 1

print(first, second, end = " ")

for i in range(3, n + 1):
    third = first + second
    print(third, end = " ")
    first = second
    second = third
