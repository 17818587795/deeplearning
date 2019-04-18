import tensorflow as tf
x = tf.constant([[1.0, 2.0]])  # tf.constant 创建一个常数张量,传入list或者数值来填充，x是一个1x2的矩阵
print(x)
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))  # 返回一个大小为2*3，标准差为1的随机数矩阵，
# seed 参数表示一个整数，当设置之后，每次生成的随机数都一样，如果想每次都生成不一样，可以设置为None
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
init_op = tf.initialize_all_variables()  # 初始化所有变量

with tf.Session() as sess:  # 创建一个会话，并通过Python的上下文管理器来管理这个会话
    sess.run(init_op)
    print(sess.run(y))
