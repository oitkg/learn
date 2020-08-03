# Github方法—如何将远程仓库里的项目在本地修改后再上传提交至远程仓库

1.在本地创建一个新的文件夹

2.打开新建的工作文件夹，右键Gub bash Here

3.使用git clone 命令将远程仓库克隆至本地指定文件夹

```
git clone https://github.com/oitkg/learn.git
```

4.对克隆的文件夹内的项目进行修改，再上传至远程仓库

```
git add 01_Github.md
git commit -m "01_github技巧"
git pull --rebase origin master  #常用于多人协作，防止误改
git push -u origin master
```

注意：因为该本地仓库是从远程仓库克隆来的，所以不需要对本地仓库进行初始化以及建立本地仓库和远程仓库的链接。

