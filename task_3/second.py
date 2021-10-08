# coding:utf-8
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

text=open(r'D:\作业\python实验七\1.txt',encoding='utf-8').read()
word=jieba.cut(text)
word=' '.join(word)

font = r'C:\Windows\Fonts\FZSTK.TTF'

wc = WordCloud(font_path=font, width=800, height=600, mode='RGBA', background_color=None).generate(word)

plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(r'D:\作业\python实验七\test1.jpg')