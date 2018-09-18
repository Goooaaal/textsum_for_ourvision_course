import os
import sys
import re
from pyhanlp import *
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# 去除时间轴， 清洗数据， 并自动摘要文本
def mv_timeline(filename):
    with open('./load_srt/%s' % filename, 'r', encoding='utf-8') as f:
        content = f.read().strip().split()
        contents =''.join(content)
        #print(contents)
        sub = re.split('[0-9][0-9][0-9]+:[0-9][0-9]:[0-9][0-9]\.[0-9][0-9][0-9]-->[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9][0-9][0-9]', contents)
        text = ''.join(sub)
        text = text.lstrip(',')
        # s = SnowNLP(text)
        # print(s.summary(3))
        return HanLP.extractSummary(text, 5)
        # with open('./srt2txt/%s' % filename, 'w', encoding='utf-8')as f2:
        #     f2.write(text)
if __name__ == '__main__':
    path = r"C:\Users\Administrator\Desktop\textsum_for_ourvision_news\load_srt"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    engine = create_engine("mysql+pymysql://updater:Yuanjing123!@101.132.171.20:3306/aivision?charset=utf8",
                           encoding="utf8", poolclass=QueuePool, pool_size=100, pool_timeout=100)


    for file in files:
        sum_text = mv_timeline(filename=file)
        sum_text = str(sum_text).lstrip('[').rstrip(']')
        text = file.split('.')[0]
        print(type(sum_text))
        print(sum_text)
        conn = engine.connect()
        transction = conn.begin()
        arg = (sum_text, text)

        data = conn.execute("update tbl_info set des=%s where srcid=%s", arg)
        transction.commit()


    transction.close()
        # lines = f.read()
        # # print(lines)
        # lines = lines.split(',')[::1]
        # # print(lines)
        # for i in lines:
        #     # print(i)
        #     i = i.strip('\n')
        #     mv_timeline(filename='load_srt/%s.srt' % i, i=i)
