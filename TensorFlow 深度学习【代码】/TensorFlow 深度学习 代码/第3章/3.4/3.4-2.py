import tensorflow as tf
# placeholder 机制，用于在会话运行时动态提供输入数据
# 用placeholder定义一个位置，tf.placeholder(dtype,shape,name)
# 用placeholder定义一个位置
# 原型placeholder(dtype,shape,name)
a = tf.placeholder(tf.float32, shape=(2), name="input")
b = tf.placeholder(tf.float32, shape=(2), name="input")
result = a+b

with tf.Session() as sess:
    sess.run(result, feed_dict={a:[1.0,2.0]})
    # feed_dict是一个字典，在字典中需要给出每个用到的placeholder的取值
    # 没有提供b的值所以报错，报错信息：
    # InvalidArgumentError (see above for traceback): You must feed
    # a value for placeholder tensor 'input_1' with dtype float and shape [2]
    print(result)

