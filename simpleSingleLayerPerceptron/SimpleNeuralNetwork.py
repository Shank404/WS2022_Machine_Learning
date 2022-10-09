import numpy as np


def funcNN(a, s, w):

    # Länge Ergebnisvektor
    nCount = np.size(a)

    # Init Netzeingabe
    netVec = np.zeros(nCount)

    # Durchlaufe alle Einträge der Gewichtsmatrix
    for x in range(nCount):
        for y in range(nCount):
            # Berechnung Gewichtete Summe
            netVec[x] = netVec[x] + w[y, x] * a[y]

        # Zwischenaktivierungszustand
        a[x] = a[x] + netVec[x]

        # Aktivierungsfunktion => Heavy-Side (0,1)
        a[x] = a[x] > s[x]

    return a
