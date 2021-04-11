import jieba
txt = open("沉默的羔羊.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
Maxvalue = 0
Maxkey = ''
for key in counts:
    if counts[key] > Maxvalue:
        Maxkey = key
        Maxvalue = counts[key]
    elif counts[key] == Maxvalue:
        if key > Maxkey:
            Maxkey = key
        else :
            continue       
print(Maxkey)
