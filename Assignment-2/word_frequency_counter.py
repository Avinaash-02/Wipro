words = input().strip()
def find(word):
    dic = {}
    for i in word:
        dic[i] = dic.get(i,0)+1
    return dic
file = open('word_frquency_finder.txt','w')
ans = find(words)
file.write(str(ans))
file.close()
