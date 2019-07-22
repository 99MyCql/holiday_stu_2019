# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from tensorflow.examples.tutorials.mnist import input_data

import re
from datetime import datetime
import time
import os
import tensorflow as tf
import csv
import pandas as pd
from pandas import Series, DataFrame
from numpy import array
import numpy as np
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"



headers = ['sex','frontal_axis','vertical axis','lateral axis','sensor_id','RSSI','Phase','frequent','Label']
headers_try = ['label']

file_dir = "data_try/S1_Dataset"

def pre_data():
    data_num_total = 0
    with open('train.csv', 'w',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        for root, dirs, files in os.walk(file_dir):
            #print(root) #当前目录路径
            #print(dirs) #当前路径下所有子目录
            print(files) #当前路径下所有非目录子文件        
        for i in range(len(files)):
            #print(len(files))
            sex = files[i][-1]
            print(sex,i)
            if sex == 'M':
                sex = 1
            elif sex == 'F':
                sex = 0

            input_file = 'data_try/S1_Dataset/' + files[i]
            reader = open(input_file, 'r')

            while True:
                line = reader.readline()
                if len(line) == 0:
                    print("Finish!","Total num of the data is: ",data_num_total)
                    break
                data_num_total = data_num_total + 1
                line = line.replace('\n','')
                line = line.replace(',', ' ')

                data_pre = line.split(' ')

                for i in range(len(data_pre)):
                    data_pre[i] = float(data_pre[i])
                data = data_pre[1:8]
                data.insert(0,sex)
                result = int(data_pre[-1])
                data.insert(8, result)
                f_csv.writerow(data)
                print(data)
    f.close()
    print("finish!!!!")




def convert2onehot(data):
    # covert data to onehot representation
    
    return pd.get_dummies(data,columns=headers )


def save_new_onehot_csv():
    data = pd.read_csv("train.csv")
    new_data = convert2onehot(data)
    #print(new_data)

    #print(data.head())
    #print("\nNum of data: ", len(data), "\n")  # 1728
    # view data values
    #for name in data.keys():
    #    print(name, pd.unique(data[name]))
    #print("\n", new_data.head(2))
    new_data.to_csv("train_onehot.csv", index=False)
    print("\n\n\n\nfinish convert to onehot!!\n\n\n\n")
    
    
    
def load_data(files_):

    # use pandas to view the data structure
    #data = pd.read_csv("train2.csv", names=headers)
    if files_ == "train":
        data1 = pd.read_csv("train_onehot.csv")
    elif files_ == "test":
        data1 = pd.read_csv("test_onehot.csv")
    elif files_ == "predict":
        data1 = pd.read_csv("predict_onehot.csv")
    return data1


    

def get_weight(shape, regularizer):
    w = tf.Variable(tf.truncated_normal(shape, stddev=0.1,mean=0))
    #损失函数loss含正则化regularization
    if regularizer != None: tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w


def get_bias(shape):
    b = tf.Variable(tf.zeros(shape))
    return b


INPUT_NODE = 4449
OUTPUT_NODE = 4
LAYER1_NODE = 512
LAYER2_NODE = 32
BATCH_SIZE = 70000
LEARNING_RATE_BASE = 0.1
LEARNING_RATE_DECAY = 0.9998
REGULARIZER = 0.0001
STEPS = 10000
MOVING_AVERAGE_DECAY = 0.99
TEST_INTERVAL_SECS = 20
MODEL_SAVE_PATH="check_point"
MODEL_NAME="data_model"

def forward(x, regularizer):
    w1 = get_weight([INPUT_NODE, LAYER1_NODE], regularizer)
    b1 = get_bias([LAYER1_NODE])
    y1 = tf.nn.relu(tf.matmul(x, w1) + b1)
    
    w2 = get_weight([LAYER1_NODE, LAYER2_NODE], regularizer)
    b2 = get_bias([LAYER2_NODE])
    y2 = tf.nn.relu(tf.matmul(y1, w2) + b2)

    w3 = get_weight([LAYER2_NODE, OUTPUT_NODE], regularizer)
    b3 = get_bias([OUTPUT_NODE])
    y = tf.matmul(y2, w3) + b3
    tf.add_to_collection('pred_network', y)  # 用于加载模型获取要预测的网络结构
    return w1,b1,y1,w2,b2,y


def backward(new_data):
    step_train = 0


    new_data = new_data.as_matrix()

    new_data = new_data.astype(np.float32)  # change to numpy array and float32
    np.random.shuffle(new_data)



    x = tf.placeholder(tf.float32, [None, INPUT_NODE],name='x')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE])

    w1, b1, y1, w2, b2,y = forward(x, REGULARIZER)
    global_step = tf.Variable(0, trainable=False)

    #损失函数loss含正则化regularization
    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cem = tf.reduce_mean(ce)
    loss = cem + tf.add_n(tf.get_collection('losses'))

    #指数衰减学习率
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        len(new_data) / BATCH_SIZE,
        LEARNING_RATE_DECAY,
        staircase=True)



    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step=global_step)

    #滑动平均
    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    ema_op = ema.apply(tf.trainable_variables())

    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name='train')

    saver = tf.train.Saver()

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

        for i in range(STEPS):
            #每次读入BATCH_SIZE组数据和标签

            if(step_train > len(new_data)):
                step_train = 0

                continue
            else:
                xs = new_data[step_train:step_train+BATCH_SIZE,:4449]

                ys = new_data[step_train:step_train+BATCH_SIZE,4449:]
            step_train = step_train + BATCH_SIZE


            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})

            if i % 30 == 0:

                print("%s : after %d training step(s), loss on training batch is %.6f, learning rate is %f." % (datetime.now(),step, loss_value,learning_rate.eval()))
                #print("w1 = ", (sess.run(w1)))

                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)
    print("finish！")


def test(new_data):
    new_data = new_data.as_matrix()
    #print(type(new_data))
    new_data = new_data.astype(np.float32)  # change to numpy array and float32
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, [None, INPUT_NODE])
        y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE])
        w1, b1, y1, w2, b2, y = forward(x, None)

        xs = new_data[:, :4449]

        ys = new_data[:, 4449:]

        ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY)
        ema_restore = ema.variables_to_restore()
        saver = tf.train.Saver(ema_restore)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict={x: xs, y_: ys})
                    print("After %s training step(s), test accuracy = %g" % (global_step, accuracy_score))
                else:
                    print('No checkpoint file found')
                    return
            time.sleep(TEST_INTERVAL_SECS)


def predict(new_data):

    new_data = new_data.as_matrix() #numpy.ndarray格式

    new_data = new_data.astype(np.float32)  # change to numpy array and float32

    with tf.Graph().as_default() as tg:
        x = tf.placeholder(tf.float32, [None, INPUT_NODE])
        w1, b1, y1, w2, b2, y = forward(x, None)


        preValue = tf.argmax(y, 1)

        print("type of prevalue = ",type(preValue))

        variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        with tf.Session() as sess:
            init_op = tf.global_variables_initializer()
            sess.run(init_op)
            ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
                xs = new_data[:, 0:INPUT_NODE]
                preValue = sess.run(preValue, feed_dict={x: xs})
                print(type(preValue),len(preValue))
                #return preValue
                
                preValue = preValue + 1
                
                print(preValue)
                data1 = DataFrame(preValue)
                data1.to_csv('predict_data.csv')
                print("finish!!!")

            else:
                print("No checkpoint file found")
                return -1




def main():

    #mnist = input_data.read_data_sets("./data/", one_hot=True)
    #backward(mnist)

    #pre_data()
    
    #print("beginning!!")
    #save_new_onehot_csv()
    
    data = load_data("train")
    backward(data)

    #data = load_data("test")
    #test(data)

    #data = load_data("predict")
    #predict(data)


#After 2282 training step(s), test accuracy = 0.865252
#After 6464 training step(s), test accuracy = 0.864649
#After 7416 training step(s), test accuracy = 0.864297


#After 9278 training step(s), test accuracy = 0.971924

if __name__ == '__main__':

    main()

