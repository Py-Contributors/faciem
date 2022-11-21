import tensorflow as tf
from tensorflow.keras import layers


class VGG16(tf.keras.Model):
    def __init__(self):
        super(VGG16, self).__init__()
        self.conv1 = layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu')
        self.conv2 = layers.Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu')
        self.conv3 = layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', activation='relu')
        self.conv4 = layers.Conv2D(filters=512, kernel_size=(3, 3), padding='same', activation='relu')
        self.maxpool = layers.MaxPool2D(pool_size=(2, 2), strides=2)
        
    @tf.function
    def call(self, inputs):
        x = layers.Input()
        x = self.conv1(x)
        x = self.conv1(x)
        x = self.maxpool(x)
        
        x = self.conv2(x)
        x = self.conv2(x)
        x = self.maxpool(x)
        
        x = self.conv3(x)
        x = self.conv3(x)
        x = self.conv3(x)
        x = self.maxpool(x)
        
        x = self.conv4(x)
        x = self.conv4(x)
        x = self.conv4(x)
        x = self.maxpool(x)
        
        x = self.conv4(x)
        x = self.conv4(x)
        x = self.conv4(x)
        x = self.maxpool(x)
        
        model = tf.keras.Model(inputs=inputs, outputs=x, name='vgg16')      
        return model

