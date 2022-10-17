with open('Text/test.txt', 'r', encoding='UTF-8') as novelFile:
    novel = novelFile.read()

import jieba

novelList = list(jieba.lcut(novel))

stopwords = [line.strip() for line in open('Text/stop.txt', 'r', encoding='UTF-8').readlines()]

novelDict = {}

for word in novelList:
    if word not in stopwords:
        if len(word) == 1:  # 长度为1，不进行统计
            continue
        else:
            novelDict[word] = novelDict.get(word, 0) + 1  # 和之前的setDefault操作类似

novelListSorted = list(novelDict.items())  # 通过items()方法将字典转换为元组列表
'''
    通过lambda函数，将元组列表的第二个元素作为排序的关键字
    reverse=True表示降序排列
'''
novelListSorted.sort(key=lambda e: e[1], reverse=True)

for topWordUp in novelListSorted[:20]:  # 统计词频最高的前20个词
    print(topWordUp)