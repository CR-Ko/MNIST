import tensorflow as tf

tf.reset_default_graph()
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('/tmp/model/model.ckpt.meta')
    saver.restore(sess, tf.train.latest_checkpoint('/tmp/model/'))
    sess.run(tf.global_variables_initializer())
    all_vars = tf.trainable_variables()
    for v in all_vars:
        print("%s with value %s" % (v.name, sess.run(v)))
