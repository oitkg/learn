计算器算法疑难总结

1.框架的搭建：需要对项目由足够的了解，明确每一步需要实现的功能。

2.格式化字符串的输出与输入。

3.二维数组的便利的方法：

方法一：

```python
for i  in range(len(matrix)):
	for j in range(len(matrix[0])):
		print(matrix[i][j])
```

注意：当数组各行的长度不相同时，会报错。

基于方法一进行优化：

```python
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		print(matrix[i][j])
```

方法二（直接遍历）：

```python
for i in matrix:
	for j in i:
		print(j)
```

4.用input()函数矩阵输入，输入的矩阵变成了字符串的原因：input()函数的返回结果就是str。

```python
a = input("请输入一个矩阵：")
print(type(a))
返回值为：str
```

