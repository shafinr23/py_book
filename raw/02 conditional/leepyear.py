num = input("enter year: ")
year = int(num)
if year%100 != 0 and year % 4 == 0:
    print("this ", year," year is leep year")
elif year %100 == 0 and year % 400 == 0:
    print("this ", year, " year is leep year")
else:
    print("this ", year, " year is not leep year")

