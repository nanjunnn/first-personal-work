import jieba
data = open("pinglunshu.txt", "r", encoding="utf-8").read()
word_all = jieba.lcut(data)
words = []
words_times = {}
results = []
useless = [i.strip() for i in open("cn_stopwords.txt", encoding="utf-8").readlines()]
for i in word_all:
    if i not in useless:
        words.append(i)
for i in words:
    if len(i) != 1:
        words_times[i] = words_times.get(i,0) + 1
result = list(words_times.items())
result.sort(key=lambda x: x[1], reverse=True)
for i in result:
    t = {}
    t["name"] = i[0]
    t["value"] = i[1]
    results.append(t)
print(results)
with open('fencishu.txt', 'w', encoding='utf-8') as fi:
     fi.write(str(results))