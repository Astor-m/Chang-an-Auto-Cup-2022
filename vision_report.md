# 可视化报告



## 目录

### 1. PyOpenGL简介

### 2. PyOpenGL 3D原理

### 3. 数据分析

### 4. 3D可视化





### 1.PyOpenGL简介

**OpenGL**（英语：*Open Graphics Library*，译名：**开放图形库**或者“开放式图形库”）是用于渲染2D、3D矢量图形的跨语言、跨平台的应用程序编程接口（API）。这个接口由近350个不同的函数调用组成，用来从简单的图形比特绘制复杂的三维景象。而另一种程序接口系统是仅用于Microsoft Windows上的Direct3D。OpenGL常用于CAD、虚拟实境、科学可视化程序和电子游戏开发。

OpenGL的主要功能

1. **建立3D模型：**OpenGL除了能够处理一般的2D图形，即点、线、面的绘制外，主要任务是集合了3D立体的物体绘制函数。
2. **图形变换：**OpenGL利用基本变换以及投影变换处理图形。所谓的基本变换就是在处理2D平面图形时的平移、旋转、变比、镜像变换。投影变换就是在处理3D立体图形时的平行投影以及透视投影。通过变换方式，可以将2D的平面图形清晰明了的变换成3D的立体图形，从而在减少计算的时间的同时就能够提高了图形显示的速度。
3. **颜色模式：**OpenGL库中的颜色模型：使用较为广泛的RGBA模式以及颜色索引模式（color index）。
4. **光照、材质的设置：**OpenGL库中包含了多种光照的类型。材质是用光反射率来表示的。其原理是基于人眼的原理，场景中的物体是由光的红绿蓝的分量以及材质的红绿蓝的反射率的乘积后所形成的颜色值。
5. **纹理映射：**纹理指的是物体表面的花纹。OpenGL库中集合了对于物体纹理的映射处理方式，能够十分完整的复现物体表面的真实纹理。
6. **图像增强功能和位图显示的扩展功能：**OpenGL的功能包括像素的读写、复制外，以及一些特殊的图像处理功能：比如，融合、反走样、雾的等等特殊的处理方式。对于图像的重现和处理，可以使得效果更有真实感，逼真。
7. **双缓存功能：**OpenGL创新性的运用了双缓存形式。计算场景、生成画面图像、显示画面图像分别将其由前台缓存和后台缓存分开处理，大大提高了计算机的运算能力以及画面的显示速度。



### 2. PyOpenGL 3D原理

**3D图理论：**

我们现实中如何观察3D物体。先找到一个观察位置，然后由观察位置看向物体。调整不同的观察位置，可以看到物体不同的角度。并且与观察物体的距离发生变化，观察到的物体大小也会发生变化，产生远小近大的效果。

计算机要绘制3D效果，也模仿了我们现实中部分的观察原理。首先需要设置观察位置，然后再把物体移动到观察视野中，并且通过透视投影，让物体产生远小近大的效果。



**坐标系**

观察点：也叫摄像机

<img src="https://upload-images.jianshu.io/upload_images/9352478-0e63e5985d870f7e?imageMogr2/auto-orient/strip|imageView2/2/w/1162/format/webp" alt="img" style="zoom:80%;" />

如上图，我们需要把物体移动到摄像机空间中，这样才能看到物体。



**模型空间-模型坐标系**

模型自身的坐标系，坐标原点在模型的某一点上，一般是几何中心位置为原点，坐标系随物体移动而移动。



**摄像机空间-摄像机坐标系**

摄像机坐标系就是以摄像机本身为原点建立的坐标系，摄像机本身并不可见，它表示的是有多少区域可以被显示（渲染）。



**投影变换**OpenGL中有两种投影方式：

- 透视投影：有远小近大的效果
- 正投影：跟距离没关系，远近的同一物体一样大

如下图所示

![img](https://upload-images.jianshu.io/upload_images/9352478-bb04c7280b7e645a?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)



### 3. 数据分析

#### 自车分析

在进行建立模型坐标系时，以自车车体为原点，车道线、目标检测物体相对于自车位置变动。

```python
# 包含自车数据分析，车体绘制、信息显示
class own: 
	def __init__(self, color, head_angle)  # 逐行读取数据，初始化当前行信息
	def draw_own(self)  # 绘制当前自车车体和信息
```

如图所示：

![image-20221204134927409](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204134927409.png)



#### 路面分析

绘制路面情况，如路边台阶，公路中间带，路边树木、护栏等。这里由于数据原因，路面情况以平地作为显示。

```python
# 绘制路面
class road:
    def __init__(self)  # 初始化
    def draw_road(self)  # 绘制路面情况
```



#### 检测目标分析

通过对目标检测数据进行分析，计算出检测目标与自车的相对位置，并在相应位置绘制该目标，同时在目标上方显示该目标的类型，如car、person、Trucks等。

```python
# 目标检测类，分析目标物体航向角、长、宽、高等数据，并绘制目标物体
class obj:
    def __init__(self)
    def get_obj_info(self, sstr, obj_parameter)  # 获取目标信息
    def draw_objs(self, info_str, cfg)  # 绘制目标
```

如下图所示：

![image-20221204140450502](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204140450502.png)<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204142621876.png" alt="image-20221204142621876" style="zoom:90%;" />

目标方向计算，如下图所示：

<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204142257731.png" alt="image-20221204142257731" style="zoom:67%;" />

得到目标前进方向后，再经过三角函数运算最终得到目标的四个顶点位置，从而将这个检测目标渲染在3D空间中。



#### 车道线分析

车道线检测，根据车道线相对于自车位置，进行计算并最终渲染到3D空间中。

```python
# 车道线类，车道线数据分析、绘制等
class line:
    def __init__(self)
    def get_line_point(self, lines) # 获取车道线类型、颜色、点集
    def get_line_parameter(self, sstr, parameter_name):  # 读取车道线参数
    def draw_lines(self, info_str, cfg)  # 绘制车道线
```

如下图所示：

<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204151356410.png" alt="image-20221204151356410" style="zoom:90%;" /><img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204151430553.png" alt="image-20221204151430553" style="zoom:90%;" />



#### 驾驶环境信息分析

通过对数据进行分析，进行驾驶环境复杂度分析、风险程度分析等，并最终将信息渲染到3D空间显示。显示信息包括：

驾驶环境信息(左侧)

1. complexity_level->环境复杂程度（Complex：复杂， General：一般，Simple：简单） 复杂度值
2. danger_level-> 风险程度（High：高，sub_high：较高， General：一般， sub_low：较低， low：低） 风险值

自车信息(右侧)

1. 当前驾驶速度

```python
# 驾驶环境信息类，处理信息显示信息
class drive_information
    def __init__(self)
     def draw_text(self, info_str, complexity_level, result_c, danger_level, result_d, EYE) # 显示数据
```

如下图所示：

![image-20221204151740664](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204151740664.png)



#### 驾驶环境分析

通过数据处理进行驾驶环境复杂程度、风险程度分析，并最终绘制在3D空间中。

```python
# 复杂度、风险度分析类，分析数据，评估驾驶环境
class Assessment:
    def __init__(self)
    def belong_function_small(self, x, a, b)# 定义偏小型梯形分布函数
    def belong_function_large(self, x, a, b)# 定义偏大型梯形分布函数
    def belong_function_middle(self, x, a, b, c)# 定义中型梯形分布函数
    def GenomplexityR(self, data)# 生成场景复杂度隶属矩阵R、R1、R2、R3
    def GenDangerR1(self, obj_nums, avg_volectiys, avg_accelerations, avg_distences, avg_volumes)# 生成R1隶属矩阵
    def GenDangerR2(self, speedings, speed, yaw_rate, long_accel, lat_accel, steering_angle)# 生成R2隶属矩阵
    def GenDangerR3(self, mean_curve, road_type, lane_type, is_in_tunnel)# 生成R3隶属矩阵
    def getOneSceneComplexityElements(self, data)# 获取全部场景负载程度元素数据
    def traficElements(self, data)# 车流要素
    def stpMotionElements(self, data)# 自车运动要素
    def sceneDangerAnalysis(self, data, describe=False)
    def laneInformationElements(self, data)# 车道信息要素
    def sceneComplexityAnalysis(self, data, describe=False)
    def risk_info(self, data)# 返回分析结果
```



### 4. 3D可视化

​	通过对数据进行分析计算，最终绘制在VIsual窗口中，进行3D呈现。

![image-20221204131932989](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221204131932989.png)

```python
# 定义宏变量
IS_PERSPECTIVE = True  # 透视投影
VIEW = np.array([-0.8, 0.8, -0.8, 0.8, 1.0, 100.0])  # 视景体的left/right/bottom/top/near/far六个面
SCALE_K = np.array([0.8, 0.8, 0.8])  # 模型缩放比例
EYE = np.array([-1.0, -10.0, 12.0])  # 眼睛的位置
LOOK_AT = np.array([0.0, 0.0, 0.0])  # 瞄准方向的参考点（默认在坐标原点）
EYE_UP = np.array([0.0, 1.0, 0.0])  # 定义对观察者而言的上方（默认y轴的正方向）
WIN_W, WIN_H = 840, 480  # 保存窗口宽度和高度的变量
LEFT_IS_DOWNED = False  # 鼠标左键被按下
MOUSE_X, MOUSE_Y = 0, 0  # 考察鼠标位移量时保存的起始位置
data = pd.core.frame.DataFrame()  #保存excel数据
data_row = 0  # 读取数据的某一列


def getposture()#调整观察视角
def init() #初始化窗口
def get_info()# 获取对象(路面，车道线，自车情况)信息
def read_data()# 读取数据、返回数据和当前数据行
def set_conf()# 设置窗口参数
def draw() # 绘制3D空间
def reshape(width, height) # 改变窗口形状
def mouseclick(button, state, x, y) #鼠标点击事件
def mousemotion(x, y)# 鼠标点击拖动

# 程序入口
def main():
    glutInit()#初始化窗口
    displayMode = GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH
    glutInitDisplayMode(displayMode)
    glutInitWindowSize(WIN_W, WIN_H)#窗口大小
    glutInitWindowPosition(200, 200)#窗口显示位置
    glutCreateWindow('Visual')#窗口标题
    init()  # 初始化画布
    glutDisplayFunc(draw)  # 注册回调函数draw()
    glutIdleFunc(draw)  # 显示动画效果
    glutReshapeFunc(reshape)  # 注册响应窗口改变的函数reshape()
    glutMouseFunc(mouseclick)  # 注册响应鼠标点击的函数mouseclick()
    glutMotionFunc(mousemotion)  # 注册响应鼠标拖拽的函数mousemotion()
    glutKeyboardFunc(keydown)  # 注册键盘输入的函数keydown()
    glutMainLoop()  # 进入glut主循环
```



##### 3D可视化，见视频



































