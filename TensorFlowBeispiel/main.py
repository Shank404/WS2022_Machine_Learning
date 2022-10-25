import tensorflow as tf

# Skalar        shape=[]        dtype=int32     rank=0
tf.constant(12)

# Vector        shape=[4]       dtype=int32     rank=1
tf.constant([1, 2, 3, 4])

# 2D-Vector     shape=[3,5]     dtype=string    rank=2
tf.constant(["Hans", "Achim", "Leon"], ["Bohne", "Lünner", "Merkel", "Goat", "Rausch"])

# 3D-Vector     shape=[2,4,6]   dtype=float32   rank=3
tf.constant([0.1, 0.2], [0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

# x = tf.constant(3, name="x")
# y = tf.constant(8, name="y")
# z = tf.constant(3, name="z")
#
# p = tf.add(x, y, name="Add")
# g = tf.multiply(p, z, name="Multiply")
#
# print(g)

# tf.compat.v1.disable_eager_execution()
# x = tf.constant(3, name="x")
# y = tf.constant(8, name="y")
# z = tf.constant(3, name="z")
#
# p = tf.add(x, y, name="Add")
# g = tf.multiply(p, z, name="Multiply")
#
# with tf.compat.v1.Session() as sess:
#     output = sess.run(g)
#     print(output)
