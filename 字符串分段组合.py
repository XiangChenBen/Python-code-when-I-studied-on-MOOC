'''获得输入的一个字符串s，以字符减号(-)分割s，
将其中首尾两段用加号(+)组合后输出'''
x = input()
STR = x.split("-")  #可以用x= x.split("-") 当不适合识别
print("{}+{}".format(STR[0],STR[-1]))  #还可以用print(STR[0]+"+"+STR[-1])