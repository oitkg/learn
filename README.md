# 一、Github的创建

## 1.远程仓库的创建

点击Github主页右上角“+”的New repository，然后对其进行设置，并完成远程仓库的创建。

## 2.本地仓库的创建

### 1.下载Git Bash

下载网址为：https://git-scm.com/downloads

### 2.在命令行中输入命令，在本地进行创建仓库

命令：

①

```
echo "# learn" >> README.md  #创建一个README.md,并将# learn字符串保存在README.md中
git init  #将项目初始化，变成git可以可管理的本地仓库（将文件夹变成仓库文件夹）
git add README.md  #将README.md添加到本地仓库（为本地文件添加一个缓存区，下一步工作的准备）
git commit -m "first commit"  #将README.md打包提交到本地仓库（为打包文件添加另一个缓存区），字符串的内容为此次提交工作的描述
git remote add origin https://github.com/oitkg/learn.git  #将本地仓库与远程仓库进行关联
git push -u origin master  #将本地仓库的项目上传到远程仓库
                
```

②

```
git remote add origin https://github.com/oitkg/learn.git  #将本地仓库与远程仓库进行关联
git push -u origin master  #将本地仓库的项目上传到远程仓库
```

### 3.总结：使用Git工具将本地项目上传到远程仓库方法

```
git init  #将项目进行初始化，变成git可管理的本地仓库
git add .  #将文件添加到本地仓库中，其中'.'是将文件夹中所有的文件添加，也可进行指定文件添加
git commit -m '某次提交工作的描述'  #将所有文件（指定文件）提交到本地仓库，字符串的内容为此次提交工作的描述
git remote add origin https://xxxxxxxxxxx  #将本地仓库与远程仓库进行关联
git pull --rebase origin master  #将远程仓库和本地仓库进行合并校验，有错误会提示
git push -u origin master  #将本地仓库的项目上传到远程仓库
```

**注意**：如果第一次后在进行修改的话，不需要对项目进行初始化以及将远程仓库和本地仓库进行关联。

```
git add xxxx.xx( .)  #将文件添加到本地仓库，其中'xxxx.xx'是修改的项目；' .'是将文件夹中所有的文件添加
git commit -m '某次提交工作的描述'  #将指定文件（所有文件）提交到本地仓库，字符串的内容为此次提交工作的描述
git pull --rebase origin master  #将本地仓库和远程仓库进行合并校验，有错误会提示
git push -u origin master  #将本地仓库的项目进行上传
```



### 4.注意

如果需要在指定路径创建，则需要在命令窗口输入命令打开指定的文件夹，然后再通过命令窗口创建本地仓库。

