"""Order parameter functions. These convert a species count to an
order parameter value.
"""
def oparamDelta(count):
    delta = sum(count[id]*coeff for id,coeff in zip((0,1,2,3,4,5), (-1,-2,-2,1,2,2)))
    
    # return as a tuple
    return delta, 

def oparamAB(count):
    A = sum(count[id]*coeff for id,coeff in zip((0,1,2), (1,2,2)))
    B = sum(count[id]*coeff for id,coeff in zip((3,4,5), (1,2,2)))
    
    return A,B

oparam1D = oparamDelta
oparam2D = oparamAB