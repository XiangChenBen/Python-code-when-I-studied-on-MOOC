import wordcloud
font = r'C:\\Windows:\\Fonts:\\simhei.ttf'
c = wordcloud.WordCloud(scale=4,font_path=font,width=1000,height=860,margin=2)
#c.generate("陈斌 陈翔 肖憩 陈文云 陈灿恩 陈思颜 家庭 和睦 美好 奋斗 富裕 成功 拼搏 健康 安康 往事如意 红红火火 事业有成 子孙满堂 富贵一家 幸福美满 ")
#c.generate("陈翔 武南希 罗鸿森 Ben Nancy Jason 大B哥 567 小弟 健身达人 金融天才 社交小能手 和睦 美好 奋斗 富裕 成功 拼搏 健康 红红火火 事业有成 幸福 快乐 充实 HD HD HD 学霸 学神 CFA持证人 FRM持证人 亿万富翁 一夜暴富 ")
#c.generate("Christine 陈沛雨 会计人才 知性 迷人 魅力无限 美丽动人 成熟 上进 机智 包容 健身达人 美好 奋斗 富裕 成功 拼搏 健康  事业有成 幸福 快乐 充实 HD HD HD 学霸 学神 CPA持证人 CFA持证人 亿万富翁 一夜暴富 ")
#c.generate("杜亲妮 杜妮子 妮妮妮 爱你么么哒 mua LOVE LOVE LOVE 百年难得一遇的美女 高挑 性感 魅力无穷 万人迷 善良 有点宅 喜欢吃 喜欢躺 最爱的人是陈翔 最爱的人是陈翔 陈翔的大宝贝 会计小萌新 四级还未过 从来不挂科 银魂铁粉 小说达人 BL爱好者 9年小伙伴 fantasticBaby")
c.generate("李佳怡 加一加一 美女姐姐 魅力无限 工作认真 独立精干 成熟 性感 知性 18forever 真老大 手速飞快 2020年暴富 成功 幸福 快乐 健康 美好 奋斗 富裕 成功 拼搏 事业腾飞")
#c.to_file("家庭名字.png")
#c.to_file("FInance三少.png")
#c.to_file("Christine.png")
#c.to_file("杜.png")
c.to_file("李佳怡.png")