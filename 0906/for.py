num = int(input("输入一个正整数: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            print(num, "不是素数")
            break
    else:
        print(num, "是素数")
else:
    print(num, "不是素数")