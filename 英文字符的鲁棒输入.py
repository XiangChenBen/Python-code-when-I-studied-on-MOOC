#获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。
s = input()
x = list()
c = str()
for i in s:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) :
        x.append(i)
c = "".join(x)
print(c)