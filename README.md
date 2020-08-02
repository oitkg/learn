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
echo "# learn" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/oitkg/learn.git
git push -u origin master
                
```

②

```
git remote add origin https://github.com/oitkg/learn.git
git push -u origin master
```

### 3.注意

如果需要在指定路径创建，则需要在命令窗口输入命令打开指定的文件夹，然后再通过命令窗口创建本地仓库。