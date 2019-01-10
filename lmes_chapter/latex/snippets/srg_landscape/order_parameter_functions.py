"""Order parameter function(s). These convert a species count to an
order parameter value.
"""
def oparamAlpha(count):
    alpha = sum(count[id]*coeff for id,coeff in zip((0,), (1,)))
    
    # return as a tuple
    return alpha, 

oparam1D = oparamAlpha