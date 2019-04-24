while True:
    n = input("plsace enter a positive number : ")
    n = int(n)
    if n < 0 :
        print( n, " is e nagetive number ")
        continue
    if n == 0:
        print(n," this number is 0 ")
        break
    print("thie squere of ", n , "is ", n*n)