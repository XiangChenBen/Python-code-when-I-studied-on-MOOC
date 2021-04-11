x = input()
s = list()
sum = 0
for i in x:
    s.append(i)
s = set(s)
for i in s:
    sum += eval(i)
print(sum)