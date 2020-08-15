# 将数据写入到excel中的方法

方法一：

```python
import xlwt
import os
import xlrd
import numpy as np
f = open(r'C:\Users\HP\Desktop\data.txt','r',encoding='ANSI')  # 打开数据文本文档，注意编码格式的影响，这里用的是ANSI编码
wb = xlwt.Workbook(encoding ='ANSI') # 打开一个excel文件
ws1 = wb.add_sheet('first') # 添加一个新表
row = 0  # 写入的起始行
col = 0  # 写入的起始列
k = 0
for lines in f:  # 在f中遍历每一行  
    a = lines.split(',')   #  以','进行分割
    k+=1
    for i in range(len(a)):
        ws1.write(row, col ,a[i])  # 向Excel文件中写入每一项
        col += 1
    row += 1
    col = 0
wb.save(r"D:\临时\data.xls")
```

方法二：

```python
import pandas as pd
if __name__ == '__main__':
    file = 'C\\User\\dongml\\Desktop\\API.xlsx'  # 打开xlsx文件
    url_list = pd.read_excel(file, sheet_name='sheet1' )  # 将读取的数据放入列表中
    excle_data = {"url":[],"count":[]}  # 创建一个空白字典
    for i, url in enumerate(url_list[].values):  # 遍历列表中数据内容及其索引值
        total = fetch(url[0])
        excel_data['url'].append(url)  # 依次添加url的内容
        excel_data['count'].append(total)  # 依次添加count的内容
        print('{0},{1},{2}'.format(i,url,total))  #  设置指定位置
    excel_file = pd.DataFrame(excel_data)
    excel_file.to_excel('C\\User\\dongml\\Desktop\\API-output.xlsx,sheet_name='sheet2)  # 将DataFrame写入excel里的sheet
```

