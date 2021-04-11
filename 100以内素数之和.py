'''描述
求100以内所有素数之和并输出。 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
素数指从大于1，且仅能被1和自己整除的整数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
提示：可以逐一判断100以内每个数是否为素数，然后求和。'''
#自己想的循环模式找prime number
'''x = 0
for i in range(2,100):
    for a in range(2,i):
        if i % a == 0:
            break
    else:                   # for if beak else 模式
        x += i 
print(x)'''
#函数式找素数 利用Ture False 记住大写
def seekprime(num):
    for i in range(2,num):
        if num % i == 0 :
            return False
    return True
sum = 0
for count in range(2,100):
    if seekprime(count) :
        sum += count
print(sum)

