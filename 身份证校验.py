def checkID():    
    id = input("请输入18位身份证号码：")
    sum = 0
    if len(id) < 18 or len(id) > 18:
        print("请输入18位号码")
    else :
        for i in range(18):
            w = pow(2,i)%11
            sum = sum + eval(id[17-i]) * w
        if sum % 11 == 1 :
            print("您输入的身份证号码是正确的")
        else :
            print("您输入的身份证号码是错误的")

def FindLastNumber():
    Givenid = input("请输入前17位身份证号码：")
    sum = 0
    if len(Givenid) < 17 or len(Givenid) > 17:
        print("请输入17位号码:)
    else :
        for i in range(1,18):
            w = pow(2,i)%11
            sum = sum + eval(Givenid[17-i])*w
        sum = sum % 11
        Lastnumber = (12 - sum) % 11
        if Lastnumber == 10:
            print("最后一个数字是X")
        else :
            print("最后一个数字是{}".format(Lastnumber))

def main():
    b = input("输入1查询身份证是否正确，输入2查询身份证最后一位（第18位）：")
    try:
        if eval(b) == 1:
            checkID()
        elif eval(b) == 2:
            FindLastNumber()
        else :
            print("请只输入1或2")
            main()
    except:
        print("请只输入1或2")
        main()

main()           
