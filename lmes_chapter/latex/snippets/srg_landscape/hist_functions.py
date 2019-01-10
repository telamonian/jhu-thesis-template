"""Basic histogram manipulation functions.
Assumes that the histograms are dictionaries with keys (x0, x1, ..., xn)
that represent discrete states and values m that represent the number 
of times each state was observed
"""
def addHists(h0, h1, weight=1.0):
    """Add two hists together
    """
    hsum = dict(h0)
    for obs,val in h1.items():
        h0[obs] = h0.get(obs, 0) + val*weight
    
    return hsum
    
def calcOParamHist(h, oparam):
    """Produce a new hist from `h` in which all of the states have been 
    transformed to their corresponding order parameter value.
    Transforms the states using the passed-in `oparam` function
    """
    oparamHist = {}

    for count,val in h.items():
        opval = oparam(count)
        oparamHist[opval] = oparamHist.get(opval, 0) + val

    return oparamHist

def normHist(h, scale=1.0):
    """Normalizes a hist such that sum(hist.values())==1
    """
    histsum = sum(list(h.values()))
    return {obs:scale*val/histsum for obs,val in h.items()}

def sparseToDense1D(h):
    """Takes a 1D hist in the dictionary (ie sparse) representation 
    and produces an array (ie dense) representation of the same hist
    """
    # sort the (observation, val) pairs in the sparse histogram
    hsorted = sorted([(obs[0], val) for obs,val in h.items()])

    # split the observations and values into their own sequences
    edges,dense = [np.array(data) for data in zip(*hsorted)]
    
    return dense,edges