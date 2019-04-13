# result = 0
# for i in range(50):
#     result = result+1
# print(result)


result = 0

# for i in range(50):
#     result = result + num
#     num = num + 1

# for i in range(51):
#     result = result + i

# for num in range(2,51):
#     result += num
#
# for i in range(1,20,5):
#     print(i)
for num in range(100):
    if num % 5 == 0:
        print(num)
        result += num

print(result)
