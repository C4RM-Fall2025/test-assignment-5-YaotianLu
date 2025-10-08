import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):

    n = m * ppy
    r = y / ppy
    c = face * couponRate / ppy
    t = np.arange(1, n + 1)

    pvcoupons = c / (1 + r) ** t
    pvface = face / (1 + r) ** n
    price = np.sum(pvcoupons) + pvface

    duration = (np.sum(t * pvcoupons) + n * pvface) / price

    return duration / ppy
