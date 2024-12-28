import tensorflow as tf
import numpy as np

def file_transport():
    from sys import argv
    name = []
    if(len(argv) == 1):
        print("Set arguments")
        exit()
    for i in range(len(argv)):
        if(i == 0):
            pass
        else:
            name.append(argv[i])
    return name[0]

def keras(a1, a2):
    a1 = a1 / a2
    model = tf.keras.models.load_model('model.keras')
    test = model.predict(np.array([a1]).reshape(1,1))
    return test

def normal(a1):
    q1 = 2
    not_prime_number = False
    while((q1 < a1)):
        if(not(a1%q1)):
            not_prime_number = True
            break
        if(q1 <= 4):
            q1 += 1
        else:
            q1 += 2
    if(not_prime_number == False):
        return 1
    elif(not_prime_number == True):
        return 0

def value(was):
    file = open("value","r")
    value = float(file.readline())
    file.close()
    return was / value

def main():
    number = float(file_transport())

    keras_value = keras(number,value(number))
    normal_value = normal(number)

    print(f"Keras model: {keras_value}")
    print(f"Normal: {normal_value}")

if(__name__ == "__main__"):
    main()