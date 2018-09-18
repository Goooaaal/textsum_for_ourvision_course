from snownlp import SnowNLP
import os

def textsum(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()
        s = SnowNLP(contents)
        sub = s.summary(5)
        # sub = sub[::-1]
        text = ','.join(sub)
        text = text.lstrip(',').strip()
        with open('./srt2txt/textsum/textsum2.txt', 'a', encoding='utf-8') as f2:
            f2.write(text)
            f2.write('\n')
            f2.write('--' * 70)
            f2.write('\n')
            f2.write('\n')
            f2.write('\n')
            f2.write('\n')




for i in range(1, 2005):
    textsum('./srt2txt/%d.txt' % i)