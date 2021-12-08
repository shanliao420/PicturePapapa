import json
import re

import requests
data = []


print("        ░██                         ░██░░        ")
print("  ██████░██       ██████   ███████  ░██ ██  ██████    ██████")
print(" ██░░░░ ░██████  ░░░░░░██ ░░██░░░██ ░██░██ ░░░░░░██  ██░░░░██")
print("░░█████ ░██░░░██  ███████  ░██  ░██ ░██░██  ███████ ░██   ░██")
print(" ░░░░░██░██  ░██ ██░░░░██  ░██  ░██ ░██░██ ██░░░░██ ░██   ░██")
print(" ██████ ░██  ░██░░████████ ███  ░██ ███░██░░████████░░██████ ")
print("░░░░░░  ░░   ░░  ░░░░░░░░ ░░░   ░░ ░░░ ░░  ░░░░░░░░  ░░░░░░ ")

print()
print()
print()
so = input("请输入搜搜关键字：")
qingxidu = input("选择图片清晰度数字： （1. 原图 2. 一般清晰度）")
size = input("输入需要爬的图片大致数量：(>=20)")

def getData(page):
    url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start={}&xml_len=20&query={}'.format(page,so)
    strHtml = requests.get(url)
    jsonData = json.loads(strHtml.text)
    data.extend(jsonData["data"]['items'])

for i in range(0,eval(size),20):
    getData(i)
    print("获取到第 %d 页数据....." % i)



list = []
conut = 1

try:
    for item in data:
        if eval(qingxidu) == 1:
            result = {
                'imgUrl':item['oriPicUrl'],
                'imgName':item['title']
            }
            list.append(result)
        else:
            result = {
                'imgUrl': item['locImageLink'],
                'imgName': item['title']
            }
            list.append(result)
        print("已解析 %d 条数据...." % conut)
        conut += 1
except Exception:
    print(conut)
count = 0
save_size = 0
for i in list:
    try:
        img = requests.get(i['imgUrl'])
        result = re.sub("[!\%\[\]\,\.\<\>\《\》\：\:\!\@\#\$\%\^\&\*\。\.\?\(\)\/\“\"]", "", i['imgName'])
        f = open("%s.jpg" % result, 'wb')
        f.write(img.content)
        f.close()
        save_size += 1
        print("以爬取 %d 张图片...." % save_size)
    except Exception:
        count += 1;
        print("出错记录 %d 条" % count)
