import os
import numpy as np
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator
import  matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
def process(name):
    print(name)
    dic = {}
    f = open('../data/'+name, 'r', encoding ='utf-8')
    s = ''
    for line in f:
        for c in line:
            if c.isalpha() and ord(c) > 255:
                #print(c+' ', end='')
                s += ''+c+'_ '
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1
    #print(dic)
    return dic, s


txtlist = os.listdir(os.getcwd()[:-3]+'data')
print(txtlist)
tdic = {}
s = ''
for file in txtlist:
    if file[-3:] == 'txt':
        dic, t = process(file)
        s += t
        for w in dic.keys():
            if w in tdic:
                tdic[w] += dic[w]
            else:
                tdic[w] = dic[w]
#print(tdic)
tlist = [[x, tdic[x]] for x in tdic]
tlist.sort(key=lambda x: -x[1])
#print(tlist)

image = np.array(Image.open('test.jpg')) 
#print(s)
my_wordcloud = WordCloud(scale=4,mask=image,background_color='white', font_path = 'simkai.ttf').generate_from_frequencies(tdic)
if os.path.exists('../output') == False:
    os.mkdir(os.getcwd()[:-3]+'output')
my_wordcloud.to_file('../output/词云.jpg')
plt.clf()
plt.bar([x[0] for x in tlist[:40]], [x[1] for x in tlist[:40]])
plt.savefig('../output/词频排行.jpg')

f = open('../output/rank.txt', 'w', encoding='utf-8')
for x in tlist:
    print(x[0], '\t', x[1], file=f)
f.close()
