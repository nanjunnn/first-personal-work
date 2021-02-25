import requests
import re

head = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

cursor = '0'
source = '1614136297251'
list1 = []
list_re = []
m = 300
for i in range(0, m):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" \
            + cursor +"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + source
    html = requests.get(url, headers=head).content.decode()
    list1111 = re.findall('"content":"(.*?)"', html, re.S)
    list_re = list_re + list1111
    print("完成度为%d" % (i))
    cursor ="".join(re.findall('"last":"(.*?)"', html, re.S))
    source = str(int(source)+1)
str_result = "\n".join(list_re)
with open('pinglunshu.txt', 'w', encoding='utf-8') as fi:
    fi.write(str_result)
print('保存成功')