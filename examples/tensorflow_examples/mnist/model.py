import tensorflow as tf
# reset everything to rerun in jupyter
tf.reset_default_graph()
# config
batch_size = 100
learning_rate = 0.01
training_epochs = 10
# load mnist data set
from tensorflow.examples.tutorials.mnist import input_data

def train(dataset_path):
    mnist = input_data.read_data_sets(dataset_path, one_hot=True)
    # input images
    # None -> batch size can be any size, 784 -> flattened mnist image
    x = tf.placeholder(tf.float32, shape=[None, 784], name="x-input")
    # target 10 output classes
    y_ = tf.placeholder(tf.float32, shape=[None, 10], name="y-input")
    # model parameters will change during training so we use tf.Variable
    W = tf.Variable(tf.zeros([784, 10]))
    # bias
    b = tf.Variable(tf.zeros([10]))
    # implement model
    # y is our prediction
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    # specify cost function
    # this is our cost
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    # Accuracy
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # specify optimizer
    # optimizer is an "operation" which we can execute in a session
    train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
    with tf.Session() as sess:
        # variables need to be initialized before we can use them
        sess.run(tf.initialize_all_variables())
        # perform training cycles
        for epoch in range(training_epochs):
            # number of batches in one epoch
            batch_count = int(mnist.train.num_examples / batch_size)
            for i in range(batch_count):
                batch_x, batch_y = mnist.train.next_batch(batch_size)
                # perform the operations we defined earlier on batch
                sess.run([train_op], feed_dict={x: batch_x, y_: batch_y})
            if epoch % 2 == 0:
                print("Epoch: ", epoch)
        print("Accuracy: ", accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
        print("done")
