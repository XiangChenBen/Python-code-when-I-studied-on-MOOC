f = open("latex.log")
count = 0
colunms=0
for line in f:
    line = line.strip("\n")
    if len(line) == 0:
        continue
    else:
        colunms += len(line)
        count += 1
result = colunms / count
print("%.0f" % result)    