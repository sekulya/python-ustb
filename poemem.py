import csv
from PIL import Image, ImageDraw, ImageFont
import random
import re
import string

poem = csv.reader(open('name.csv', encoding="GBK"))    # 读入csv文件
names = []
for item in poem:
    # 将文件的每一项都加入到list中
    names.append(item[0])
# 将文件中的每一项加入list中

poem = open('tang.txt', 'r', encoding='utf-8')  # 读入txt文件
lines = poem.readlines()
poem.close()

names_dict = {}
for name in names:
    name = '赠'+name    # 构建诗名
    content = []
    which_p = []
    for i in range(4):
        estring = name[i]+'[^，。（）！？《》：；””]{6}[，。！？]'  # 构建诗句的正则表达式
        e1 = re.compile(estring)
        estring = '【[^】]*】'  # 构建诗名的正则表达式
        e2 = re.compile(estring)
        poem_n = ""
        find_result = []
        # 根据正则表达式寻找结果并加入list
        for line in lines:
            line = line.replace(u'\u3000', u' ')
            if(e2.findall(line) != []):
                poem_n = line[line.find('【'):line.rfind("\\")]
            if(e1.findall(line) != []):
                result = [poem_n, e1.findall(line)[0]]
                find_result.append(result)
        result = random.choice(find_result) # 利用random函数挑选结果
        # 重构标点符号
     
        if i % 2 == 0:
            result[1] = result[1][0:7]+'，'
        else:
            temp = random.randint(0, 2)
            punctuation = ['。', '？', '！']
            result[1] = result[1][0:7]+punctuation[temp]
        content.append(result)
    names_dict[name] = content  # 最终加入字典

for name in names_dict:
    num=random.randint(1,10) # 使用random函数挑选背景图片
    img = Image.open('background/'+str(num)+'.png')
    img=img.resize((800,1000))  # 使用resize函数调整背景图片大小
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font='MoRanXingKai-2.ttf', size=34)

    # 信头部分
    draw.text(xy=(200,150),text="亲爱的",fill=(0,0,0),font=font)
    draw.text(xy=(308,150),text=name[1:],fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),font=font)
    draw.text(xy=(400,150),text="：",fill=(0,0,0),font=font)
 

    # 诗的部分
    i=0
    for si in names_dict[name]:
        draw.text(xy=(170,251+i*51),text=si[1][0],fill=(random.randint(0,256),random.randint(0,256),random.randint(0,256)),font=font)
        draw.text(xy=(170,251+i*51),text=si[1][0],fill=(256,0,0),font=font)
        draw.text(xy=(207, 251+i*51), text=si[1][1:], fill=(0, 0, 0), font=font)
        i=i+1

    # 备注人
    draw.text(xy=(450,450),text="作者：李世民",fill=(0,0,0),font=font)

    # 收入邮箱
    email_len=random.randint(5,10)
    email_start=random.sample(string.ascii_letters+string.digits,email_len)
    email_end=random.choice(('@163.com','@qq.com'))
    email=''.join(email_start)+email_end
    email_font=ImageFont.truetype(font='MoRanXingKai-2.ttf', size=36)
    draw.text(xy=(150,650),text="邮箱\n"+email,fill=(0,0,0),font=email_font)

    # 信尾部分
    draw.text(xy=(550,650),text="思亲赫",fill=(0,0,0),font=font)
    draw.text(xy=(550,700),text="2021/6/27",fill=(0,0,0),font=font)

    # 保存图片
    file_path="card/"+name+".png"
    img.save(file_path)
