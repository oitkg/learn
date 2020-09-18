# 2 .python新建excel写入数据

使用openpyxl库，xird库只能读取excel内容，openpyxl库不支持老版本office2003的xls格式。

1.openpyxl的基本用法

```python
import openpyxl

# 创建一个excel workbook对象
book = openpyxl.Workbook()

# 创建时，会自动生成一个sheet，通过active获取
sh = book.active

# 修改当前sheet，名为为工资表
sh.title = '工资表'

# 保存文件
book.save('信息.xlsx')

# 增加一个名为'年龄表'的sheet，放在最后
sh1 = book.create_sheet('年龄表')

# 增加一个sheet，放在前面
sh2 = book.create_sheet('年龄表-最前', 0)

# 增加一个sheet，指定为第二个表单
sh3 = book.create_sheet('年龄表-指定', 1)

# 根据名称获取某个sheet对象
sh = book['工资表']

# # 对上述操作进行保存
# book.save('信息.xlsx')

# 给第一个单元格写入内容
sh['A1'] = '你好'

# 根据行号列号，给一个单元格写入内容，注意和xlrd，是从1开始的。
sh.cell(2, 2, value='我很好')
sh.cell(2, 3).value = '你好吗'

print(sh.cell(2, 2).value)
book.save('信息.xlsx')

# 获取某个单元格的内容
print(sh['A1'].value)
```

注意：每次操作完一定要save。

2.修改excel数据

```python
import openpyxl

wb = openpyxl.load_workbook('年龄表.xlsx')

sheet = wb['年龄表']
sheet['A1'] = '战将'
wb.save('年龄表（修改）.xlsx')
```

实例（将字典中的年龄内容写入到excel文件中）：

```python
import openpyxl

name2Age = {
    '张飞': 38,
    '赵云': 27,
    '许褚': 36,
    '典韦': 38,
    '关羽': 39,
    '黄忠': 49,
    '徐晃': 43,
    '马超': 23
}

# 创建一个excel workbook对象
book = openpyxl.Workbook()

# 创建时，自动生成一个sheet，通过active获取
sh = book.active

sh.title = '年龄表'

# 写标题栏
sh['A1'] = '姓名'
sh['B1'] = '年龄'

# 写入内容
row = 2

for name, age in name2Age.items():
    sh.cell(row, 1).value = name
    sh.cell(row, 2).value = age
    row += 1

# 保存文件
book.save('年龄表.xlsx')
```

