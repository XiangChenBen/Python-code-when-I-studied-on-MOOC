def getnum():
    nums = []
    iNumStr = input("Please input a number(press enter to quit):")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("Please input a number(press enter to quit):")
    return nums
def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s/len(numbers)
def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev += (num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getnum()
m = mean(n)
print("mean:{:.3f},sample standard deviation:{:.3f},median:{}".format(m,dev(n,m),median(n)))