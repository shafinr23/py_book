mark = input("your marks:")
marks = int(mark)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else:
    grade = "F"
print("your Grade is " , grade)
