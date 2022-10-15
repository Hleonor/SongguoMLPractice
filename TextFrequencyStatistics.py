with open('Text/test.txt', 'r', encoding='UTF-8') as novelfile:
    novel = novelfile.read()

import jieba

novellist = list(jieba.lcut(novel))

stopwords = [line.strip() for line in open('Text/stop.txt' , 'r' , encoding='UTF-8').readlines()]

noveldict = {}

for word in novellist:
    if word not in stopwords:
        if len(word) == 1:  # 长度为1，不进行统计
            continue
        else:
            noveldict[word] = noveldict.get(word, 0) + 1  # 和之前的setDefault操作类似

novellistsorted = list(noveldict.items())
novellistsorted.sort(key = lambda e:e[1] , reverse = True)

topwordnum = 0
for topwordup in novellistsorted[:20]:
    print(topwordup)