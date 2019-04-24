terminate = False
while not terminate:
    num1 = input("enter 1st number ")
    num1 = int(num1)
    num2 = input("enter 2nd number ")
    num2 = int(num2)
    while True:
        opration = input("want to add or sub . to qite thsi programm type quite ")
        if opration == "quit":
            print("programe close")
            terminate = True
            break
        if opration not in ["add","sub"]:
            print(" type current oprator")
            continue
        if opration == "add":
            print(num1, " and ", num2 ,"added and resut is ", num1+num2)
            break
        if opration == "sub":
            print(num1, " and ", num2, "subed and resut is ", num1 - num2)
            break