# deep learning 03

[TOC]

## 1. 卷积网络初识

> 卷积神经网络（Convolutional Neural Networks, CNN）是一类包含卷积计算且具有深度结构的前馈神经网络（Feedforward Neural Networks），是深度学习（deep learning）的代表算法之一

### 1.1. 出现缘由

在神经网络中，每一层的每个神经元都与下一层的每个神经元相连，这种连接关系叫全连接(Full Connected)。

但这种方法用在**图像处理**上，效率太低了。而卷积神经网络的出现，大大提高了图像处理的效率。

它主要包括**卷积层(convolutional layer)**和**池化层(pooling layer)**。

### 1.2. 卷积层

#### 1.2.1. 图片数据

首先，对于一张图片，它相当于一个三维结构。

每个像素点对应三个或N个`int8`的值，如RGB图像的一个白色像素点对应`(256, 256, 256)`。

一张 32x32x3 的图片，长度和宽度为32，深度为3，则有 32x32x3 个`int8`的值。

#### 1.2.2. 卷积核

卷积层的基本单位是**卷积核(filter)**：

- 卷积核是一个三维结构

- 卷积核的长、宽由用户自定义

- 深度需要与图片的深度相同

每个卷积层可以有多个卷积核。

### 1.3. 卷积运算

#### 1.3.1. 单卷积核运算

假设有一个 5x5 的图像(深度暂略)，使用一个 3x3 的filter进行卷积，想得到一个 3x3 的Feature Map，如下所示：

![1](./images/readme1.png)

其运算过程为：

![2](./images/readme2.gif)

该过程中，长宽方向的**步幅**都为1，即长宽方向每次移动一格。

从运算的每次移动中，我们发现图像的中间区域提取次数较多，边缘部分提取次数较少，怎么办呢？

一般方法是在图像外围加一圈0，增加的0圈数也称作**Zero Padding**。

#### 1.3.2. 卷积层运算

再假设输入一张 5x5x3 的图片，采用两个 3x3x3 的卷积核进行运算，并对图片外围增加一圈0变成 7x7x3 ，如下：

![3](./images/readme3.gif)

运算过程的**步幅**为2，最终**输出是一个三维结构(类似于输出一张图片)**，长宽为3(步幅为2，长宽只够运算三次)，深度为2(该层有两个卷积核)。

卷积层运算就是将每个卷积核运算的结果合并在一起。

与神经网络相同，卷积运算结束后还要加上偏置参数，并调用激活函数。

### 1.4. 池化

池化(Pooling)其效果就是将样本缩小。

池化的方法很多，最常用的是Max Pooling。Max Pooling实际上就是在 **NxN 的样本**中**取最大值**，作为采样后的样本值。下图是 2x2 max pooling：

![4](./images/readme4.png)

除了Max Pooing之外，常用的还有 Mean Pooling (取各样本的平均值)。

## 2. Tensorflow 实现卷积网络

与神经网络不同的是，在构建**全连接神经网络之前**，还得构建卷积神经网络。

示例如下：

```py
# 卷积运算
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME') # 步长为1，补零

# 池化
def max_pool_2x2(x):
    return tf.nn.max_pool2d(x, ksize=[1,2,2,1],strides=[1,2,2,1], padding='SAME') # 2x2池化 步长为2 补零

# 初始化权重(卷积核)
def weight_variable(shape):
    init = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(init)

# 初始化偏置参数
def bias_variable(shape):
    init = tf.constant(0.1, shape=shape)
    return tf.Variable(init)

# 构建网络
def cnn(x):
    x_image = tf.reshape(x, [-1,28,28,1])     # 不定数个 28x28x1 图片
    # 第一层卷积
    w1 = weight_variable([5,5,1,32]) # 32个 5x5x1 卷积核
    b1 = bias_variable([32])
    conv1 = tf.nn.relu(conv2d(x_image,w1) + b1) # 1个 28x28x32
    pool1 = max_pool_2x2(conv1)                 # 1个 14x14x32

    # 第二层卷积
    w2 = weight_variable([5,5,32,64]) # 64个 5x5x32 卷积核
    b2 = bias_variable([64])
    conv2 = tf.nn.relu(conv2d(pool1, w2) + b2) # 1个 14x14x64
    pool2 = max_pool_2x2(conv2)                # 1个 7x7x64

    # 全连接网络
    wfc1 = weight_variable([7*7*64, 1024])
    bfc1 = bias_variable([1024])

    # 把卷积网络中的4维图像转为二维图像
    p2 = tf.reshape(pool2, [-1, 7*7*64])
    fc1 = tf.nn.relu(tf.matmul(p2,wfc1) + bfc1)

    # 防止过拟合
    keep_prob = tf.placeholder(tf.float32)
    dfc1 = tf.nn.dropout(fc1, keep_prob)

    # 输出层
    wfc2 = weight_variable([1024,10])
    bfc2 = bias_variable([10])
    out = tf.matmul(dfc1, wfc2) + bfc2
    return out, keep_prob
```

卷积网络介绍和简单示例见：

- [1-卷积神经网络CNN(Convolutional_Neural_Network).ipynb](1-卷积神经网络CNN(Convolutional_Neural_Network).ipynb)

Tensorflow中卷积和池化函数的使用：

- [2-卷积和池化基础.ipynb](2-卷积和池化基础.ipynb)

案例见：

- [3-卷积神经网络应用于MNIST数据集分类.ipynb](3-卷积神经网络应用于MNIST数据集分类.ipynb)

- [基于Tensorflow的交通标志识别.ipynb](基于Tensorflow的交通标志识别.ipynb)

- cnn-digit-recognition-tensorflow

参考博客:

- [https://www.zybuluo.com/hanbingtao/note/485480](https://www.zybuluo.com/hanbingtao/note/485480)

- [https://blog.csdn.net/weixin_42451919/article/details/81381294](https://blog.csdn.net/weixin_42451919/article/details/81381294)
