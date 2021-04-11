def fbnq(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbnq(n-1)+fbnq(n-2)
x = eval(input("please input an intger that is bigger than 1:"))
print(fbnq(x))