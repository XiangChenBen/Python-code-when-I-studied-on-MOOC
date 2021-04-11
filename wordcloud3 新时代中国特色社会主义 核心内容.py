import jieba
import wordcloud
from imageio import imread
mask = imread("fivestar.png")
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "C:\\Windows:\\Fonts:\\simhei.ttf",mask = mask,width=1000,height = 700, background_color="white")
w.generate(txt)
w.to_file("新时代中国特色社会主义核心词汇.png")