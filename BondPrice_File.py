import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy                    
    r = y / ppy                    
    c = face * couponRate / ppy    

    t = np.arange(1, n + 1)        
    pvcoupons = np.sum(c / (1 + r) ** t)  
    pvface = face / (1 + r) ** n         

    return pvcoupons + pvface

