fo = open("output.txt","w+")
ls = ["China","America","Franch","\n","SSS"]
print(ls)
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()