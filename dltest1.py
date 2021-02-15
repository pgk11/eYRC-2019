import tensorflow as tf
g1 = tf.Graph()
with graph1.as_default():
    a = tf.constant([45.6], name = 'constant_a')
    b = tf.constant([3], name = 'constant_b')
