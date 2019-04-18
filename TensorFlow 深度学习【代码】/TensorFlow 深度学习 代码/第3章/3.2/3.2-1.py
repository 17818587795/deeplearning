import tensorflow as tf
a = tf.constant([1.0, 2.0], name="a")            # 常量是一种输出值永远固定的计算
b = tf.constant([3.0, 4.0], name="b")           # tf.constant 创建一个常数张量,传入list或者数值来填充
print(a)
result = a+b                                        # 常量相加的计算
print(result.graph)
print(a.graph is tf.get_default_graph())          # 通过graph属性可以获取张量所属计算图
print(b.graph is tf.get_default_graph())           # tf.get_default_graph() 获取当前默认计算图
# 输出True
   # True
