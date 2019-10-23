"""Ingest the raw data you'll need to calculate the landscape from the
simulation output SFile
"""
import re
from robertslab.sfile import SFileProto

basinRe = re.compile('Basins/(\d*)')
stageRe = re.compile('Stages/(\w*)')
phaseRe = re.compile('Phases/(\d*)')

basinEdges = {}
basinPhaseHists = {}
basinMFPTs = {}
basinPhaseWeights = {}
basinTrajectoryCounts = {}

# open the simulation output and show a progress bar
with SFileProto.open('data/srg_-_out.sfile', progress=True) as f:
    phaseHists = {}

    # iterate through each record in the output
    for rec in f.records():
        # determine the basin and stage during which the record was written
        basin = int(basinRe.search(rec.name).group(1))
        stage = stageRe.search(rec.name).group(1)

        if stage != 'Production':
            # if this isn't a record from a production stage, skip it
            continue

        if rec.dataType.find('SpeciesTimeSeries') > -1:
            # determine the phase during which the record was written
            phase = int(phaseRe.search(rec.name).group(1))

            # fetch the phaseHists for this basin
            basinPhaseHists[basin] = phaseHists = \
                basinPhaseHists.get(basin, dict())

            # add to the count of the appropriate phaseHist
            phaseHists[phase] = phaseHist = phaseHists.get(phase, dict())

            # increment the values of the phaseHist based on the species count
            # samples in the record
            for count in (tuple(row) for
                          row in rec.msg(unpackNDArray=True)[1]['counts']):
                phaseHist[count] = phaseHist.get(count, 0) + 1

        elif rec.dataType.find('StageOutputSummary') > -1:
            # get the first passage times and the phase weights
            # from the StageOutputSummary record
            summaryMsg = rec.msg()
            basinEdges[basin] = np.array(summaryMsg.edges)
            basinMFPTs[basin] = np.array(summaryMsg.first_passage_times)
            basinPhaseWeights[basin] = np.array(summaryMsg.weights)

        elif rec.dataType.find('StageOutputRaw') > -1:
            # get the trajectory counts from the StageOutputRaw record
            rawMsg = rec.msg()
            basinTrajectoryCounts[basin] = \
                np.array(rawMsg.final_trajectory_ids) -  \
                np.array(rawMsg.first_trajectory_ids) + 1
