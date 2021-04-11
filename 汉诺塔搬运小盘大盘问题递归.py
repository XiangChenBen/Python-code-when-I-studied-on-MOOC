count = 0
def hanoi(n,ori,des,mid):
    global count
    if n == 1 :
        print("{}:{}->{}".format(1,ori,des))
        count += 1
    else :
        hanoi(n-1,ori,mid,des)
        print("{}:{}->{}".format(n,ori,des))
        count += 1
        hanoi(n-1,mid,des,ori)
x = eval(input("please input the number of plat:"))
hanoi(x,'A','C','B')
print(count)