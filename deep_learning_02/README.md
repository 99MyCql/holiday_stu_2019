# deep_learning_01

[TOC]

## 1. 案例分析

- 病害猪肉预测 - 分类问题

- 股票预测 - 回归问题

- 老年人动作识别 - 分类问题

## 2. Tensorflow 变量

详情见 [1-深入理解TensorFlow变量.ipynb](1-深入理解TensorFlow变量.ipynb)

[参考博客](https://www.jianshu.com/p/c69f25fcc4a4)

## 3. Tensorboard 可视化

详情见：

- [2-Tensorboard 基础.ipynb](2-Tensorboard基础.ipynb)

- [3-tensorboard基础案例.ipynb](3-tensorboard基础案例.ipynb)

- [4-Tensorflow监控指标可视化.ipynb](4-Tensorflow监控指标可视化.ipynb)

- [5-tensorboard可视化.ipynb](5-tensorboard可视化.ipynb)

Tensorboard 的启动过程可以概括为以下几步：

1. 创建writer，写日志文件

```py
writer=tf.summary.FileWriter('/path/to/logs/', tf.get_default_graph())
```

2. 保存日志文件

```py
writer.close()
```

3. 运行可视化命令，启动服务

```bash
tensorboard –-logdir=/path/to/logs/
```

## 4. 模型保存

两种方式：

- `ckpt`文件，详情见 [9-TensorFlow模型文件ckpt.ipynb](9-TensorFlow模型文件ckpt.ipynb)

- `pd`文件，详情见 [10-pb文件保存方法.ipynb](10-pb文件保存方法.ipynb)
