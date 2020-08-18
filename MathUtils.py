import math

# https://en.wikipedia.org/wiki/Sigmoid_function
def Sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))