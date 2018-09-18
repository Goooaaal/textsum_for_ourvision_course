# encoding: utf-8
import xdrlib, sys
import xlrd
from CxExtractor import CxExtractor

def load_excel(file_path):
    workbook = xlrd.open_workbook(file_path)
    booksheet = workbook.sheet_by_name('Sheet1')
    for i in range(1, 10):
        cell_i7 = booksheet.cell_value(i, 7)
        if not cell_i7.strip():
            continue
        return cell_i7
       cell_i2 = booksheet.cell_value(i, 1)
       cell_i3 = booksheet.cell_value(i, 2)
       print(cell_i7)
        with open('data_excel_text/url.txt', 'a') as f:
            f.writelines(cell_i7)
            f.write('\n')
        cx = CxExtractor(threshold=186)
        html = cx.readHtml('HTML/read.html', coding='utf-8')
        content = cx.filter_tags(html)
        # print(content)
        with open('Text/(%d).txt'%(i + 2000), 'w', encoding='utf-8') as f:
            f.write('标题:%s 摘要:%s 内容:%s'%(cell_i1, cell_i2, content.strip().split()))
load_excel('data_excel/excel.xls')
# cx = CxExtractor(threshold=186)
# html = cx.readHtml('HTML/read.html', coding='utf-8')
# content = cx.filter_tags(html)
# #print(content)
# with open('Text/126.txt', 'w', encoding='utf-8') as f:
#     f.writelines(content.strip().split())
# #print(cx.getText(content))
# #print(s)
