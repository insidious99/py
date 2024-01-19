print("First pattern: ")
for i in range(4):
    for j in range(10):
        print("*", end = "")
    print()
    
print("Second pattern")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end = "")
    print()
    
print("Third pattern")
for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end = '')
    for k in range(1, i + 1):
        print("*", end = '')
    print()
    
print("Fourth pattern")
for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end = "")
    for k in range(1, 2 * i):
        print("*", end = "")
    print()
    

print("Fifth pattern")
for i in range(1,6):
    for j in range(5 ,i, -1):
        print(" ", end = "")
    for k in range(1, 2 * i):
        print(i, end = "")
    print()
    

print("Sixth pattern")
for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end = "")
    for k in range(i,0,-1):
        print(k, end = "")
    for l in range(2,i+1):
        print(l, end = "")
    print()+
