from keras.datasets import mnist
from matplotlib import pyplot

# loading the dataset and storing into different variables
(train_X, train_y), (test_X, test_y) = mnist.load_data()