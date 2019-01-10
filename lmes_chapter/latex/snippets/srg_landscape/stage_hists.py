"""create the stage hists by reweighting and combining the phase hists.
One stage hist will be created per basin set in the simulation's input
"""
basinIDs = sorted(basinPhaseHists.keys())

basinStageHists = {}
for bid in basinIDs:
    phaseHists = basinPhaseHists[bid]
    phaseWeights = basinPhaseWeights[bid]
    trajectoryCounts = basinTrajectoryCounts[bid]

    # calculate the weight the landscape sampled during each phase will have 
    landscapePhaseWeights = np.ones(phaseWeights.size, dtype=float)
    landscapePhaseWeights[2:] = phaseWeights[1:-1]
    landscapePhaseWeights = landscapePhaseWeights.cumprod()
    landscapePhaseWeights[1:] /= trajectoryCounts[1:]
    
    # calculate the stage hist by combining all of the phase hists
    stageHist = {}
    for phaseID,weight in enumerate(landscapePhaseWeights[1:].flat):
        addHists(stageHist, phaseHists[phaseID+1], weight=weight)
    
    basinStageHists[bid] = stageHist