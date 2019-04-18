import tensorflow as tf
# placeholder 机制，用于在会话运行时动态提供输入数据
# 用placeholder定义一个位置，tf.placeholder(dtype,shape,name)
# 用placeholder定义一个位置
# 原型placeholder(dtype,shape,name)
a = tf.placeholder(tf.float32, shape=(2), name="input")
b = tf.placeholder(tf.float32, shape=(2), name="input")
result = a+b

with tf.Session() as sess:    # 创建一个会话，并通过Python的上下文管理器来管理这个会话
    # Session.run()函数有很多参数，原型为
    # sess.run(self,fetches,feed_dict,options,run_metadata)
    # fetches参数接受result，feed_dict参数指定了需要提供的值
    # 使用这个创建好的会话来计算关心的结果
    # 在这之后，不再需要调用Session.close()函数来关闭会话， 当上下文
    # 退出时会话关闭和资源释放也自动完成了
    sess.run(result, feed_dict={a:[1.0, 2.0], b:[3.0, 4.0]})  # run()函数会运行一个会话，一般传入需要在会话内运行的计算过程
    print(result)
    # 输出Tensor("add:0", shape=(2,), dtype = float32)
