import wordcloud
font = r'C:\\Windows:\\Fonts:\\simhei.ttf'
c=wordcloud.WordCloud(scale=4,font_path=font,width=1000,height=860,margin=2)
c.generate("真的无语 为什么这么烦 我也好烦 墨迹一下午才写完一道计算题 哎 你说我们为什么这么焦虑 越来越内卷 我感觉一堆事情 "
           "我导师还说叫我们准备写论文了 我他妈课又多 作业又多 还要考专八 还要找实习 我他妈充分理解 真的好累 主要就是事情特别多 "
           "而且有些东西写起来又特别不顺心 就好tm烦躁 真的他妈的烦躁 一天到晚就是忙个要死 他妈的 社畜就算了 还是学畜 课也听不懂 妈的 "
           "最后一句给我看笑了 好他妈真实 就是因为听不懂 我就更烦躁了 真的听不懂 妈的 作业也不知道咋做 烦都烦死了 一天天的")
c.to_file("Nancy背景墙.png")