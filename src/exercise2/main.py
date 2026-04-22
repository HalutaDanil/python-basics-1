num = int(input())

if num < 0:
    print(False)
else:
    temp_num = num
    invert_num = 0
    while temp_num > 0:
        invert_num = invert_num * 10 + (temp_num % 10)
        temp_num //= 10
    print(num == invert_num)
