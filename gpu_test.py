import tensorflow as tf
tf.config.list_physical_devices('GPU')
tf.test.is_gpu_available()