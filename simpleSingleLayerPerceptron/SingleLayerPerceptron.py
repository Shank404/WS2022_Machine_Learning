import numpy as np

from SimpleNeuralNetwork import funcNN


def startNN(input1, input2, operation):

    # Gesamtanzahl Neuronen
    nCount = 3

    # Anzahl Input-Neuronen
    nInput = 2

    # Anzahl Output-Neuronen
    nOutput = 1

    # Init AND oder OR
    if operation == "AND":
        # Init AND-Schwellwert = 1.5
        s = np.array([0.5, 0.5, 1.5])
    else:
        # Init OR-Schwellwert = 0.5
        s = np.array([0.5, 0.5, 0.5])

    # Init Ergebnisvektor
    a = np.zeros(nCount)

    # Init Gewichtsmatrix
    w = np.array([[0, 0, 1], [0, 0, 1], [0, 0, 0]])  # Hinton Matrix

    # Input
    x = np.array([input1, input2])

    # Füge den Input der Ergebnismatrix hinzu
    a[:2] = x[:2]

    return funcNN(a, s, w)
