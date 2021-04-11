'''给用户三次输入用户名和密码的机会，要求如下：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
1）如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
2）当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”。'''
for i in range(1,4):
    Name = input("Please enter username:")
    Password = input("Please enter password:")
    if (Name == "Kate") and (Password == "666666") :
        print("Succeed to login in！")
        break
    elif i<3:
        print("Username or password is wrong, you have {} more chance".format(3-i))
    else : 
        print("Three tries are all wrong. Fail to login in!")
