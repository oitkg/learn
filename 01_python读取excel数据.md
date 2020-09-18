# python处理excel数据

## 1.读取数据

使用xlrd库

1.读取excel文件中的表单的数量和名称

```python
import xlrd

book = xlrd.open_workbook(r'C:\Users\HP\Desktop\income.xlsx')

print(f"包含的表单数量 {book.nsheets}")
print(f"表单的名字分别为 {book.sheet_names()}")
```

2.获取表单中的单元格数据，通过**表单索引**获取表单或者通过**表单名**获取表单

```python
sheet = book.sheet_by_index(0)

print(f"表单名:{sheet.name}")
print(f"表单索引:{sheet.number}")
print(f"表单列数: {sheet.nrows}")
print(f"表单行数: {sheet.ncols}")
```

3.获取sheet后，使用cell_value方法，参数为行号和列号，读取指定单元格的文本内容。

```python
import xlrd

sheet = book.sheet_by_index(0)

print(f"单元格A1内容是: {sheet.cell_value(rowx=5, colx=1)}")
```

4.获取指定行列的数据，获取指定行使用row_value方法，获取指定列使用col_value方法。

```python
import xlrd

sheet = book.sheet_by_index(0)

print(f"第一行的内容: {sheet.row_values(0)}")
print(f"第一列的内容: {sheet.col_values(0)}")
print(f"不要第一行的内容: {sheet.col_values(0, start_rowx=1)}")  # 获取指定范围内的数据
```

实例1：

```python
"""计算2017年的收入总额"""
import xlrd

sheet = book.sheet_by_index(0)
income = sheet.col_values(1, start_rowx=1)

print(income)
print(f"2017年的总收入是: {int(sum(income))}")



"""计算2017年中月份不包含带星号的收入总额"""
import xlrd

sheet = book.sheet_by_index(0)
incomes = sheet.col_values(1, start_rowx=1)

print(income)
print(f"2017年的总收入是: {int(sum(income))}")


# 去掉包含星号的月份收入
toSubstract = 0
# 读取月份，在第一列
monthes = sheet.col_values(colx=0)

for row, month in enumberate(monthes):
    if type(month) is str and month.endwith("*"):
        income = sheet.cell_value(row, 1)
        print(month, income)
        toSubstract += 1
        
print(f"2017年真实收入: {int(sum(incomes) - toSubstract)}")        
```

实例2（计算excel中所有sheet的总收入）：

```python
import xlrd

book = xlrd.open_workbook('income.xlsx')

sheets = book.sheets()

incomeOf3years = 0
for sheet in sheets:
    # 收入在第二列
    incomes = sheet.col_values(1, start_rowx=1)
    # 去掉包含星号的月份收入
    toSubstract = 0
    # 月份在第一列
    monthes = sheet.col_values(colx=0)

    for row, month in enumerate(monthes):
        if type(month) is str and month.endwith('*'):
            income = sheet.cell_value(row, 1)
            print(month, income)
            toSubstract += income

    actualIncome = int(sum(incomes) - toSubstract)
    print(f"{sheet.name}年的真实收入: {actualIncome}")
    incomeOf3years += actualIncome

print(f"总收入: {incomeOf3years}")
```

