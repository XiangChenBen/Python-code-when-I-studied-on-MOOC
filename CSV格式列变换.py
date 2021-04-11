#附件是一个CSV文件，请将每行按照列逆序排列后输出，不改变各元素格式（如周围空格布局等）。
'''f = open("data.csv")
ls = list()
for line in f:
    line = line.strip("\n")
    line = line.split(",")
    line = line[::-1]
    line = ",".join(line)
    ls.append(line)
for item in ls:
    print(item)'''
#优化版：
'''f = open("data.csv")
for line in f:
    line = line.strip("\n")
    ls = line.split(",")
    ls = ls[::-1]
    print(",".join(ls))
f.close()'''
#附件是一个CSV文件，其中每个数据前后存在空格，请对其进行清洗，要求如下：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#（1）去掉每个数据前后空格，即数据之间仅用逗号(,)分割；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#（2）清洗后打印输出。
'''f = open("data.csv")
ls = list()
for line in f:
    line = line.replace("\n","")
    line = line.replace(" ","")
    ls.append(line)
for item in ls:
    print(item)'''
#优化版：
'''f = open("data.csv")
ls = f.read()
ls = ls.replace(" ","")
print(ls)
f.close()'''
#1）按行进行倒序排列；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#（2）每行数据倒序排列；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#（3）使用分号（;）代替逗号（,）分割数据，无空格；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
#按照上述要求转换后将数据输出。
f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
for line in ls:
    line = line.strip("\n")
    line = line.replace(" ","")
    line = line.split(",")
    line = line[::-1]
    print(";".join(line))
f.close()
    
