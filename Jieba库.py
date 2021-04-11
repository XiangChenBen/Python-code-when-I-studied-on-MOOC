import jieba
s = "中华人民共和国是伟大的"
print(jieba.lcut(s)) #['中华人民共和国', '是', '伟大', '的']
print(jieba.lcut(s)[1]) #是
print(jieba.lcut(s,cut_all=True))  #['中华', '中华人民', '中华人民共和国', '华人', '人民', '人民共和国', '共和', '共和国', '国是', '伟大', '的']
print(jieba.lcut_for_search(s))  #['中华', '华人', '人民', '共和', '共和国', '中华人民共和国', '是', '伟大', '的']