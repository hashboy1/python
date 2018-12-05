# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

# 在tensorflow中，所有变量必须用tf.Variable定义，0为初始值,name为该变量名称（可选）
state = tf.Variable(0, name='counter')
# print(state.name)
one = tf.constant(1)

# 与new_vale = state + 1等价，tf中必须用专有函数操作，且下述语句仅是定义该操作，并不执行
new_value = tf.add(state, one)
# 指定将new_value的值更新到state，这里依然是事先指定这个操作给变量update，并不会执行
update = tf.assign(state, new_value)

# 指定tf启动session时要进行所有变量初始化操作，这里依然只是指定初始化操作给init，并不实际执行
# 换句话说，只要上面存在tf.Variable（）的调用，就必须调用init操作
init = tf.global_variables_initializer()

# 启动tf会话并执行
with tf.Session() as sess:
    sess.run(init)  # 所有tf.Vaiable()定义的变量被真正初始化
    # print('-' * 8, sess.run(state))
    # 测试变量更新操作，执行多次
    for _ in range(10):
        sess.run(update)  # 变量更新操作
        print(sess.run(state))  # 输出state值，注意tf中要查看某个变量的值同样需要用sess.run()函数