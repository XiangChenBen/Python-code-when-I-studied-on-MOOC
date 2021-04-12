import wordcloud
font = r'C:\\Windows:\\Fonts:\\simhei.ttf'
c=wordcloud.WordCloud(scale=4,font_path=font,width=1000,height=860,margin=2)
c.generate("   ")
c.to_file("背景墙.png")
