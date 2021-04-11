#打印输出附件文件的有效行数，注意：空行不计算为有效行数。
'''w = open("latex.log")
s = 0
for line in w:
    line = line.strip("\n")
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))'''
#统计附件文件的小写字母a-z的字符分布，即出现a-z字符的数量，并输出结果。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#同时请输出文件一共包含的字符数量。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#注意输出格式，各元素之间用英文逗号（,）分隔。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#答案可能包含a-z共26个字符的分布，如果某个字符没有出现，则不显示，输出顺序a-z顺序。
'''w = open("latex.log")
dist = {}
sum = 0
for line in w:
    for word in line:
        sum += 1
        if word in "qwertyuiopasdfghjklzxcvbnm":
            dist[word] = dist.get(word,0)+1
print("共{}字符".format(sum),end="")
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in dist.keys():
        print(",{}:{}".format(i,dist[i]),end="")'''
#统计附件文件中与其他任何其他行都不同的行的数量，即独特行的数量。
w = open("latex.log")
alllines = w.readlines() 
s = set(alllines) #全集
for i in s:
    alllines.remove(i) #寻找化成全集时被消去的重复元素
rept = set(alllines) #被削去的元素集合
result = s - rept
print("共{}独特行".format(len(result)))