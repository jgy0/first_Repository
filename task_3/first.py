from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np

#词云生成
text=open(r'D:\xinjianqq\MobileFile\新时代中国特色社会主义(1).txt','r',encoding='gbk').read()


word= jieba.cut(text)  #text为你需要分词的字符串/句子

string = ' '.join(word)
string=string[:100]

font = r'C:\Windows\Fonts\FZSTK.TTF'
img = Image.open(r'D:\photo\ps素材\wordcoud.png')
img_array = np.array(img)

wc = WordCloud(font_path=font, width=800, height=600, mode='RGBA',mask=img_array, background_color=None).generate(string)




#wordcloud = WordCloud(font_path=font,max_words=20,mask=img_array,background_color='white').generate(text)

plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(r'D:\作业\python实验七\test.jpg')