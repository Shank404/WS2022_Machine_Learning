import tensorflow
from tensorflow.python.keras import Input, Model
from tensorflow.python.keras.layers import ReLU, MaxPooling2D, Dense, Softmax
from tensorflow.python.keras.legacy_tf_layers.convolutional import Conv2D
from tensorflow.python.keras.utils.vis_utils import plot_model

imageInput = Input(shape=(28, 28, 1))

conv1 = Conv2D(8, kernel_size=(3, 3), padding="same")(imageInput)
batch1 = tensorflow._compat.BatchNormalization()(conv1)
relu1 = ReLU()(batch1)

maxPool1 = MaxPooling2D()(relu1)

conv2 = Conv2D(16, kernel_size=(3, 3), padding="same")(maxPool1)
batch2 = tensorflow._compat.BatchNormalization()(conv2)
relu2 = ReLU()(batch2)

maxPool2 = MaxPooling2D()(relu2)

conv3 = Conv2D(32, kernel_size=(3, 3), padding="same")(maxPool2)
batch3 = tensorflow._compat.BatchNormalization(conv3)
relu3 = ReLU()(batch3)

dense = Dense(10)(relu3)
softmax = Softmax()(dense)

model = Model(inputs="imageInput", outputs="softMax")
#model.compile(optimizer='sgd', loss=CategoricalCrossentropy())

print(model.summary())
# plot graph
plot_model(model)

