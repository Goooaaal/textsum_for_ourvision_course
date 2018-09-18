from bs4 import BeautifulSoup
import requests
from gevent import monkey
monkey.patch_all()
import sys
import os
from gevent.pool import Pool
import pandas as pd
import re




## aliyun下载srt, 并写入文件夹
def download(url, file_name):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Window NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36'
    }

    file_name += '.txt'
    try:
        r = requests.get(url, headers=headers)
        with open('./load_srt/' + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
                print(file_name + '    is ojbk')
        # with open('./load_srt/' + file_name, 'w') as f:
        #     f.write(r.content)
        # print(file_name + '    is ojbk')
    except Exception:
        pass





if __name__ == '__main__':
    ## 从csv文件中取出srt链接
    csv_path = './src_link.csv'
    csv_data = pd.read_csv(csv_path)
    try:
        for i, j in zip(list(csv_data['srt_ch']), list(csv_data['srcid'])):
            url = 'https://youtube-ch.oss-cn-shanghai.aliyuncs.com/' + i
            download(url=url, file_name=j)

    except Exception:
        pass