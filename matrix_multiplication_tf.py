# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:01:11 2017

matrix multiplication in tensorflow

y = x * w

@author: Farhana Ferdousi Liza
"""

import numpy as np
import tensorflow as tf


#define placeholder
x = tf.placeholder(tf.float32, [3, 4])
w = tf.placeholder(tf.float32, [4, 5])

# add an op to initialize the variables
init_op = tf.global_variables_initializer()


# define model
mul = tf.matmul(x,w)

# Generate some data
x_rand_normal = np.random.normal(0.0,0.1, (3,4))
w_rand_normal = np.random.normal(0.0,0.5, (4,5))

# session starts 
sess = tf.Session()
k = sess.run(init_op)
y = sess.run(mul, feed_dict={x:x_rand_normal, w:w_rand_normal})

# print result
print(k)
print(y, type(y))  
