# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:41:48 2018

@author: XinYuan
"""

import tensorflow as tf


print('Laoded TF Version',tf.__version__)


v1 = tf.Variable(10)
v2 = tf.Variable(5)
addv = v1 + v2
print(addv)
print(type(addv)) #<class 'tensorflow.python.framework.ops.Tensor'>
print(type(v1))  #<class 'tensorflow.python.ops.variables.Variable'>


# 用来运行计算图谱的对象
# Session is a runtime
# 和Java web中的session是否有相似之处？
sess = tf.Session()


# Variable -> 初始化 -> 有值的tensor

tf.initialize_all_variables().run(session = sess)

print('变量是需要初始化的')
#两种运行方式
print('加法（v1,v2）=',addv.eval(session = sess))
print('加法（v1,v2）=',sess.run(addv))


c1 = tf.constant(10)
c2 = tf.constant(5)
addc = c1 + c2;


print('c1 + c2 = ',addc.eval(session=sess))
# constant 实际上是 Tensor
print(type(c1)) #<class 'tensorflow.python.framework.ops.Tensor'>
print(type(addc)) #<class 'tensorflow.python.framework.ops.Tensor'>

'''
这种定义操作，再执行操作的模式，被称为“符号式编程” Symbolic Programming

先定义 addc addv操作 再在session中执行 session相当于执行操作的容器、环境？
'''



print('---------------------------------------------')

graph = tf.Graph()
with graph.as_default():
    value1 = tf.constant([1,2])
    value2 = tf.Variable([3,4])
    mul = value1*value2

with tf.Session(graph=graph) as mySess:
    #tf.initialize_all_variables().run(session=mySess) #初始化所有变量
    tf.initialize_all_variables().run() #with下可以省略
    print('value1 * value2 = ',mySess.run(mul))
    #print('value1 * value2 = ',mul.eval(session=mySess))
    print('value1 * value2 = ',mul.eval())


print('-------------use placeholder---------------------')


def load_from_remote():
    return [-x for x in range(1000)]


'''
    自定义的generator

    partial 局部的
'''
def load_partial(value,step):
    index = 0
    while index < len(value):
        yield value[index:index+step]
        index += step
    return


graph = tf.Graph()

with graph.as_default():
    value1 = tf.placeholder(dtype=tf.float64)
    value2 = tf.Variable([3,4],dtype=tf.float64)
    mul = value1 * value2

with tf.Session(graph=graph) as mySess:
    tf.initialize_all_variables().run()
    # 假设数据来自远端
    value = load_from_remote()
    for partialValue in load_partial(value,2):
        holderValue = {value1:partialValue} #为value1赋值
        #evalResult = mul.eval(feed_dict=holderValue)
        runResult = mySess.run(mul,feed_dict=holderValue)
        #print('value1 * value2 = ',evalResult)
        print('value1 * value2 = ',runResult)
