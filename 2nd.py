import string
import regex as re
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np
from matplotlib.pyplot import *
#pylab = pyplot + numpy
f=open("text1.txt","r",encoding='utf-8')
txt=f.read()
#将所有字母更改为小写，消除单词重复测量中大小写对比的阻抗
txt=txt.lower()
#在排列组合分词策略中，不同的生僻字和重音符号用空格代替
for ch in string.punctuation:
    txt=txt.replace(ch," ")
#根据空格对文本进行切分
words=txt.split()
#制作运动统计字典
result={}
for word in words:
    result[word]=result.get(word,0)+1
#排序将字典转换为列表
items=list(result.items())
#根据单词的频数从高到低排序
items.sort(key=lambda x:x[1],reverse=True)
#求单词总数
len=len(items)
print(len)
#输出全部
print(items)
#输出排序结果中位于前10位的单词
for i in range(5):
    print(items[i])
x=np.linspace(1, len, len)
y=np.zeros_like(x)
for i in range(len):
    y[i]=items[i][1]
print(x)
print(y)

plt.figure()
plt.plot(x, y, 'r.')
plt.xlabel('sort')
plt.ylabel('amount')
plt.title('sort-amount')
plt.show()

pat = "\\b(\\w+led)\\b"
m = re.findall(pat, txt)
print(m)
