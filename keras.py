import tensorflow as tf
import numpy as np
import pandas as pd

def normalization(was):
    value = 1.0
    while(not(np.max(was) < 1)):
        was = was / 10.0
        value *= 10.0
    return was, value

def keras_model(x,y):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=(x.shape[1],)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(124, activation='relu'))
    model.add(tf.keras.layers.Dense(32, activation='relu'))
    model.add(tf.keras.layers.Dense(1,activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    model.fit(x,y,epochs=2, validation_split=0.1, batch_size=5)
    model.save("model.keras")

def data_preparing():
    data_x = pd.read_csv('x.csv',sep=',', header=None)
    data_x = data_x.values
    data_y = pd.read_csv('y.csv',sep=',',header=None)
    data_y = data_y.values

    x = np.array(data_x)
    y = np.array(data_y)
    x = x.astype(float)
    y = y.astype(int)
    x = x.flatten()
    x = x[:-1]
    y = y.flatten()
    y = y[:-1]

    x, value = normalization(x)
    file = open("value", "w")
    file.write(f"{value}")
    file.close()
    x = np.array([data_x])
    y = np.array([data_y])
    x = x.reshape(-1,1)
    y = y.reshape(-1,1)
    x = x[:-1]
    y = y[:-1]
    return x,y

def main():
    x, y = data_preparing()
    keras_model(x,y)
    return 0

if(__name__ == "__main__"):
    main()