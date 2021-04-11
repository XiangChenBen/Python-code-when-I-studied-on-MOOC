#BMI in domestic and nationaL
height, weight = eval(input("请输入身高（m）体重（kg）用逗号隔开)："))
BMI = weight / pow(height,2)
print("BMI is: {:.2f}".format(BMI))
domestic, internationaL= "",""
if BMI < 18.5:
    domestic, international = "little slim", "little slim"
elif BMI < 24:
    domestic, international = "normal","normal"
elif BMI < 25:
    domestic, international = "normal ","little fat"
elif BMI < 28:
    domestic, international = "little fat","little fat"
elif BMI < 30:
    domestic, international = "little fat","fat"
else :
    domestic, international = "fat","fat"
print("domestically, it is '{0}', internationally, it is '{1}'".format(domestic,international))