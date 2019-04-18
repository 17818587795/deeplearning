import tensorflow as tf
    # weights = tf.constant([[1.0, 2.0]])
    #
    # # regularizer_l2是l2_regularizer()函数返回的函数
    # regularizer_l2 = tf.contrib.layers.l2_regularizer(0.5)
    # # TensorFlow会将L2的正则化损失值除以2使得求导得到的结果更加简洁
    # # regularizer_l1是l1_regularizer()函数返回的函数,0.5表示正则化的权重，tf.contrib.layers.l1_regularizer(0.5)表示正则化式子
    # regularizer_l1 = tf.contrib.layers.l1_regularizer(0.5)
    # with tf.Session() as sess:
    #     print(sess.run(regularizer_l2(weights)))
    #     # 输出7.5
    #     print(sess.run(regularizer_l1(weights)))
    #     # 输出5.0