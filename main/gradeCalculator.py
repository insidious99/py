# Python program to enter marks and get a grade and percentage
# Change maxm (maximum marks) and marks > 400 accordingly.

print("Percentage and Grade calculator for Pre Board Exam")
eng = float(input("Enter your marks for English: "))
hin = float(input("Enter your marks for Hindi: "))
sst = float(input("Enter your marks for SST: "))
sci = float(input("Enter your marks for Science: "))
mat = float(input("Enter your marks for Maths: "))

marks = ( eng + hin + sst + sci + mat)
maxm = 400
total = marks / maxm
percentage = total * 100

if marks > 400:
    print("Invalid marks obtained")
elif percentage >= 90:
    print("Your grade is A1 with a percentage of ", percentage)
elif percentage >= 80:
    print("Your grade is A2 with a percentage of ", percentage)
elif percentage >= 70:
    print("Your grade is B1 with a percentage of ", percentage)
elif percentage >= 60:
   print("Your grade is B2 with a percentage of ", percentage)
elif percentage >= 50:
    print("Your grade is C1 with a percentage of ", percentage)
elif percentage >= 40:
    print("Your grade is C2 with a percentage of ", percentage)
else: 
    print("Your failed with a percentage of ", percentage)
