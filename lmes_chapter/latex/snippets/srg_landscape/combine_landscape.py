# initialize the hist that will cover the entire landscape by 
# starting with the transition region hist
landscapeHist = dict(transitionHist)

# get the range of the transition region, in terms of the 
# 1D order parameter values
oparamvals = [oparam1D(count) for count in landscapeHist.keys()]
opmin,opmax = min(oparamvals), max(oparamvals)

# add the non-overlapping data from the left and 
# right hists to the transition hist
for count,val in phaseZeroSideHists[0].items():
    opval = oparam1D(count)
    if opval < opmin:
        if count in landscapeHist: raise KeyError
        landscapeHist[count] = sideLandscapeWeights[0]*val
for count,val in phaseZeroSideHists[1].items():
    opval = oparam1D(count)
    if opval > opmax:
        if count in landscapeHist: raise KeyError
        landscapeHist[count] = sideLandscapeWeights[1]*val
landscapeHist = normHist(landscapeHist)