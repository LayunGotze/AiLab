from django.shortcuts import render
import requests
import json
import tensorflow as tf
import os, base64
from PIL import Image
import numpy as np
from django.http import JsonResponse
# Create your views here.


def test(request):
    msg=request.GET.get('msg','success')
    return JsonResponse({"msg":msg})


def mnist(request):
    bs64_str = request.POST.getlist('image')
    img_data = base64.b64decode(bs64_str[0].split(',')[1])

    # 转换为np数组
    file = open('temp.jpg', "wb")
    file.write(img_data)
    file.close()
    ans = process()
    return JsonResponse({"res": ans})


def cast(url):
    im = Image.open(url)
    im = im.resize((28, 28)).convert("LA")
    matrix = np.asarray(im)
    list = []
    for i in range(0, 28):
        temp = []
        for j in range(0, 28):
            temp.append(255 - matrix[i][j][0])  # / matrix[i][j][1]
        list.append(temp)
    data = np.matrix(list)
    return data


def process():
    sess = tf.InteractiveSession()

    # 占位符
    x = tf.placeholder("float", shape=[None, 784], name="Mul")
    y_ = tf.placeholder("float", shape=[None, 10], name="y_")
    # 变量
    W = tf.Variable(tf.zeros([784, 10]), name='x')
    b = tf.Variable(tf.zeros([10]), 'y_')

    # 权重
    def weight_variable(shape):
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    # 偏差
    def bias_variable(shape):
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    # 卷积
    def conv2d(x, W):
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


    # 最大池化
    def max_pool_2x2(x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                              strides=[1, 2, 2, 1], padding='SAME')

    # 相关变量的创建
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    # 激活函数
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    keep_prob = tf.placeholder("float", name='rob')
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    # 用于训练用的softmax函数
    y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2, name='res')
    # 用于训练作完后，作测试用的softmax函数
    y_conv2 = tf.nn.softmax(tf.matmul(h_fc1, W_fc2) + b_fc2, name="final_result")

    # 交叉熵的计算，返回包含了损失值的Tensor。

    # cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
    # 优化器，负责最小化交叉熵
    # train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

    # correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    # 计算准确率
    # accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    # 初始化所以变量
    # sess.run(tf.global_variables_initializer())

    # 保存输入输出，可以为之后用
    # tf.add_to_collection('res', y_conv)
    # tf.add_to_collection('output', y_conv2)
    # tf.add_to_collection('x', x)


    # 将当前图设置为默认图
    # graph_def = tf.get_default_graph().as_graph_def()
    # # 将上面的变量转化成常量，保存模型为pb模型时需要,注意这里的final_result和前面的y_con2是同名，只有这样才会保存它，否则会报错，
    # # 如果需要保存其他tensor只需要让tensor的名字和这里保持一直即可
    # output_graph_def = tf.graph_util.convert_variables_to_constants(sess,
    #                                                                 graph_def, ['final_result'])
    # # 保存前面训练后的模型为pb文件
    # with tf.gfile.GFile("grf.pb", 'wb') as f:
    #     f.write(output_graph_def.SerializeToString())

    # # 用saver 保存模型
    saver = tf.train.Saver()
    # saver.save(sess, "model_data/model")
    saver.restore(sess, "model_data/model")

    # 导入图片，同时灰度化
    im = cast("temp.jpg")
    x_img = np.reshape(im, [-1, 784])
    output = sess.run(y_conv2, feed_dict={x: x_img})
    # print('the predict is : ', np.argmax(output))
    return int(np.argmax(output))
