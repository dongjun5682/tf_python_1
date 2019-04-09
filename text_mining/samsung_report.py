from konlpy.tag import Okt
import pandas as pd

# import nltk
# nltk.download()
import re
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

okt = Okt()
ctx = '../data/'
filename = ctx + 'kr-Report_2018.txt'
stopword = ctx + 'stopwords.txt'

with open(filename, 'r', encoding='utf8') as f:
    texts = f.read()

texts = texts.replace('\n', '')  # 줄바꿈 없애버림
tokenizer = re.compile(r'[^ ㄱ-힣]+')  # r-> 읽어들인다 / [^ ㄱ-힣]+ 한글을 제외한 모든글자
texts = tokenizer.sub('', texts)
tokens = word_tokenize(texts)

noun_tokens = []
for t in tokens:
    t_pos = okt.pos(t)
    t2 = [i[0] for i in t_pos
          if i[1] == 'Noun']
    if len("".join(t2)) > 1:
        noun_tokens.append("".join(t2))
texts = " ".join(noun_tokens)

with open(stopword, 'r', encoding='utf-8') as f:
    stopwords = f.read()

stopwords = stopwords.split(' ')
texts = [text for text in tokens if text not in stopwords]

frequtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)

okt.pos('가치창출')
okt.pos('갤럭시')

wcloud = WordCloud(ctx + 'D2Coding.ttf', relative_scaling=0.2
                   , background_color='white').generate(" ".join(texts))

plt.figure(figsize=(12, 12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
