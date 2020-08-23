# GitHub上删除项目的操作

1.在本地master文件夹中打开Git Bash Here

2.

```
git pull origin master  # 将远程仓库的项目拉取下来
```

3.

```
dir -la  # 查看文件夹以及文件，使用-la显示更直观
```

4.

```
git rem -r --cached 文件名称  # 删除指定文件
```

5.

```
git commit -m 'delete指定文件'  # 提交并添加操作说明
```

6.

```
git push -u origin master  # 将本次更改更新到github项目上
```

