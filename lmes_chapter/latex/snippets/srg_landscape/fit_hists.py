import scipy.optimize as opt

# fit the left and right hists seperately to the transition hist
transitionHist1D = calcOParamHist(transitionHist, oparam1D)
sideLandscapeWeights = []
for pzHist in phaseZeroSideHists:
    pzHist1D = calcOParamHist(pzHist, oparam1D)

    # define a Jensen-Shanon divergence (symmetrized KL divergence) function
    # for the minimizer
    def _jsdiv(x):
        div = 0

        for opval in (opval for opval in transitionHist1D.keys()
                      if opval in pzHist1D):
            transval,pzval = transitionHist1D[opval], x*pzHist1D[opval]

            # iterate only over states in which both hists contain
            # at least some density
            if transval==0 or pzval==0:
                continue

            meanval = .5*(transval + pzval)
            div += .5*(transval*np.log(transval/meanval)
                       + pzval*np.log(pzval/meanval))

        return div

    # start the fitting weight at 2.0
    weightFit0 = 2.0

    # fit by minimizing the difference between the transition hist and the
    # section of the phase zero hist that overlaps with the transition hist
    weightFitOut = opt.minimize(_jsdiv, x0=weightFit0, method='Nelder-Mead')
    sideLandscapeWeights.append(weightFitOut.x[0])

# print some info about the fit of the left and right sides of the landscape
print('The left side of phase zero will have a weight of: %.3f'
      % sideLandscapeWeights[0])
print('The right side of phase zero will have a weight of: %.3f'
      % sideLandscapeWeights[1])
