
## 结构：

```
.
├── data_excel      // 新闻的存储文件
│   
├── load_srt   // 将下载后的字幕文件保存
│   
├── Text    // 文本摘要后的摘要文本
│
├── clean_text //下载后的新闻文本清洗，提取正文
├── load——srt.py //下载课程的字幕文件
├── src_link //课程字幕文件的地址
├
├── move_timeline   // 去除时间轴信息，并自动摘要课程主题提取

```





## 项目配置

**系统需要安装：**

- requests    ---爬虫框架
- beautifulsoup     ---web提取框架
- jieba      ---分词、词性标注
- pandas    ---数据科学工具
- HanLP   ---开源NLP工具包
- sqlalchemy  ---MySQL python操作包





