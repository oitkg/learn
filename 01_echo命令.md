# Shell echo命令

描述：用来控制字符串的输出，通常echo可以实现更复杂的字符串输出

## 1.显示普通字符串

```
echo "It is a test"
```

结果为：

```
It is a test
```

注意：双引号可以省略不写

## 2.显示转义字符

```
echo "\"It is a test""
```

结果为：

```
"It is a test"
```

注意：双引号可以省略不写

## 3.显示变量

```
#！/bin/sh  #对shell进行声明，说明你用的哪种类型的shell以及路径所在
read name 
echo "$name It is a test"
```

将以上代码保存为test.sh, name接收标准输出的变量，结果是：

```
[root#www. ~]# sh test.sh  #root是登陆账户，www是主机名。~是目录所在的位置（当前显示是根目录），#表示管理员登录，执行脚本的时候用sh + 脚本名
OK  #标准输入
OK It is a test  #输出
```

## 4.显示换行

``` 
echo -e "OK! \n" # -e 开启转义
echo "It is a test" 
```

结果为：

```
OK！
It is a test
```

## 5.显示不换行

```
#！/bin/sh
echo -e "OK! \c"  # -e 开启转义 \c 不换行
echo It is a test
```

结果为：

```
OK！It is a test
```

## 6.显示结果定向至文件

```
echo "It is a test" > myfile
```

## 7.原样输出字符串，不进行转义或取变量

```
echo '$name\"'
```

结果为：

```
$name\"
```

注意：使用单引号

## 8.显示命令执行结果

```
echo `date`
```

结果为：显示当前日期

注意：使用的是反引号``，而不是''

## 9.Shell中 '>' 和  '>>'的区别和联系

'>' 是创建：echo "hello shell" > out.txt

'>>' 是追加：echo "hello shell" >>out.txt

当out.txt不存在时，'>' 和 '>>' 都会默认创建一个out.txt,并将hello shell字符串保存至out.txt文件中。

当out.txt存在时，'>' 会将out.txt文件中的内容清空，再把hello shell字符串保存至out.txt文件；'>>' 时将hello shell 追加到out.txt文件内容的末尾。