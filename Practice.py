dayfactor=0.01
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("dayup power is {:.2f}, daydown power is {:.2f}".format(dayup,daydown))
