# Prime-numbers
## How to use
Install TensorFlow, pandas and NumPy.
```
pip install -r requirements.txt
```
Generate the dataset, first argument is a last number, second is a first number.
```
python3 data_generator.py 100000 1
```
Edit the Keras model if needed, then train it.
```
nano keras_machine_learning.py
python3 keras_machine_learning.py
```
Finally you can compare trained model with standard algorithm for searching for prime numbers e.g. 5.
```
python3 comparison.py 5
```
