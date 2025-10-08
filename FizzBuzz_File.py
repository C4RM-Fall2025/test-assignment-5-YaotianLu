import numpy as np

def FizzBuzz(start, finish):

    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)

    mask3 = (numvec % 3 == 0)
    mask5 = (numvec % 5 == 0)
    mask15 = mask3 & mask5

    objvec[mask3] = "fizz"
    objvec[mask5] = "buzz"
    objvec[mask15] = "fizzbuzz"

    return objvec
