# matplotlib的基本使用

## 1.matplotlib基础用法

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linepace(-1,1,50)
# y = 2*x + 1
y = x ** 2
plt.plot(x,y)
plt.show()  # 展示绘图
```

注意：保存格式为.png

## 2.figure图像

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x ** 2

plt.figure()
plt.plot(x,y1)

plt.figure(num = 3, figsize(5,3))  # 指定figure的编号、长高大小
plt.plot(x,y2)
plt.plot(x,y1,color="red",linewidth=1.0.linestyle="--")

plt.show()
```

注意：1.plt.figure() 定义后，之后的代码块都属于这个flt.igure（）

2.有多少plt.figure()，就会打印多少张图。

## 3.设置坐标轴

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x ** 2

plt.figure()  # 指定figure的编号、长高大小
plt.plot(x,y2)
plt.plot(x,y1,color="red",linewidth=1.0,linestyle="--")
 
plt.xlim((-1,2))  # 设置x坐标轴的范围（-1，2）
plt.ylim((-2.,3))  # 设置y坐标轴的范围（-2，3）
plt.xlabel("x坐标轴")  # 设置x坐标轴的名称
plt.ylabel("y坐标轴")   # 设置y坐标轴的名称

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)  # 设置x轴的单位
plt.yticks([-2,-1.8,-1,1.22,3], [r"$really\ bad$",r"$bad$",r"$normal$",
                                 r"$great$",r"$really\ great$"])  # 设置y坐标轴的文字，并将文字设为好看的字体

plt.show()
```

注意：

1."$xxx$"可以优化字体

2.\ +空格可以在图中编译出空格。\ \ + 特殊字符的英文名称可以编译出特殊符号

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x ** 2

plt.figure()  # 指定figure的编号、长高大小
plt.plot(x,y2)
plt.plot(x,y1,color="red",linewidth=1.0,linestyle="--")
 
plt.xlim((-1,2))  # 设置x坐标轴的范围（-1，2）
plt.ylim((-2.,3))  # 设置y坐标轴的范围（-2，3）
plt.xlabel("x坐标轴")  # 设置x坐标轴的名称
plt.ylabel("y坐标轴")   # 设置y坐标轴的名称

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)  # 设置x轴的单位
plt.yticks([-2,-1.8,-1,1.22,3], [r"$really\ bad$",r"$bad$",r"$normal$",
                                 r"$great$",r"$really\ great$"])  # 设置y坐标轴的文字，并将文字设为好看的字体

plt.show()
```

## 4.修改坐标轴的位置

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x ** 2

plt.figure()  # 指定figure的编号、长高大小
plt.plot(x,y2)
plt.plot(x,y1,color="red",linewidth=1.0,linestyle="--")
 
plt.xlim((-1,2))  # 设置x坐标轴的范围（-1，2）
plt.ylim((-2.,3))  # 设置y坐标轴的范围（-2，3）
plt.xlabel("x坐标轴")  # 设置x坐标轴的名称
plt.ylabel("y坐标轴")   # 设置y坐标轴的名称

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)  # 设置x轴的单位
plt.yticks([-2,-1.8,-1,1.22,3], [r"$really\ bad$",r"$bad$",r"$normal$",
                                 r"$great$",r"$really\ great$"])  # 设置y坐标轴的文字，并将文字设为好看的字体


# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))  # ('data',0)设置横轴在竖轴0的位置
ax.spines['left'].set_position9(('data',0))  # ('data',0)设置竖轴在横轴0的位置

plt.show()
```

## 5.Legend图例

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x ** 2

plt.figure()  # 指定figure的编号、长高大小
 
plt.xlim((-1,2))  # 设置x坐标轴的范围（-1，2）
plt.ylim((-2.,3))  # 设置y坐标轴的范围（-2，3）
plt.xlabel("x坐标轴")  # 设置x坐标轴的名称
plt.ylabel("y坐标轴")   # 设置y坐标轴的名称

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)  # 设置x轴的单位
plt.yticks([-2,-1.8,-1,1.22,3], [r"$really\ bad$",r"$bad$",r"$normal$",
                                 r"$great$",r"$really\ great$"])  # 设置y坐标轴的文字，并将文字设为好看的字体

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))  # ('data',0)设置横轴在竖轴0的位置
ax.spines['left'].set_position9(('data',0))  # ('data',0)设置竖轴在横轴0的位置

# plt.plot(x,y2,label='up')
# plt.plot(x,y1,color="red",linewidth=1.0,linestyle="--",label='down')
# plt.legend(headles=,label=,loc='best')  # loc设置图例的位置，有upeer right...

plt.plot(x,y2)
l1, = plt.plot(x,y2)
l2, = plt.plot(x,y1,color="red",linewidth=1.0,linestyle="--")
plt.legend(headles=[l1,l2,],labels=['aaa','bbb'],loc='best')  # loc设置图例的位置，有upeer right...

plt.show()
```

## 6.添加注解

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8,5),)
plt.plot(x, y,)

plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.show()

```

## 12.3D数据

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))  # rstride:行跨度，cstride:列跨度
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')  # zdir：将投影的方向，offset：将投影定义的位置
ax.set_zlim(-2,2)

plt.show()
```

## 13.Subplot多图合一

```python
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,2,1)  # 位置表述（2行2列第1个位置）
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)  # 位置表述（2行2列第2个位置）
plt.plot([0,1],[0,2])

plt.subplot(2,2,3)  # 位置表述（2行2列第3个位置）
plt.plot([0,1],[0,3])

plt.subplot(2,2,4)  # 位置表述（2行2列第4个位置）
plt.plot([0,1],[0,4])

plt.show()
```

## 14.Subplot分格显示

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

## method 1 : subplot2grid
# plt.figure()
# ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)  # (3,3)有3行3列grid；(0,0)从0行0列开始；colspan:列跨度为1列，rowspan：行跨度为3行
# ax1.plot([1,2],[1,2])
# ax1.set_title('ax1_title')
# ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
# ax3 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
# ax4 = plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
# ax5 = plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)

# # method 2 :gridspec
# plt.figure()
# gs = gridspec.GridSpec(3,3)  # 有3行3列
# ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])
# ax4 = plt.subplot(gs[-1, 0])
# ax5 = plt.subplot(gs[-1, -2])

# method 3:easy to define structure
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])

plt.show()
```

## 15.plot in plot图中图

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,2,3,4,5,6,7]

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left,bottom,width,height = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, 'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

plt.axes([0.6,0.2,0.25,0.25])
plt.plot(y[::-1],x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
```

## 16.次坐标轴

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-')   # green, solid line
ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')

ax2.plot(x, y2, 'b--') # blue
ax2.set_ylabel('Y2 data', color='b')
              
plt.show()
```

## 17.Annimation动画

```python
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=20,
                              blit=False)

plt.show()
```

