#xiang
'''x = input("please input a number between 1-7:")
WeekStr="一二三四五六天"
print("星期"+WeekStr[eval(x)-1])'''
#切片式
WeekStr = "星期一星期二星期三星期四星期五星期六星期天"
x = eval(input("please input a number between 1-7:"))
pos = (x-1)*3
print(WeekStr[pos:pos+3])