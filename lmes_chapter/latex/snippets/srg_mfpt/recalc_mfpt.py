import numpy as np
from robertslab.sfile import SFileProto

with SFileProto.open('data/srg_-_out.sfile') as f:
    summaries = list(f.msgs(include=('production', 'summary')))

mfptRecalcs = []
for summary in summaries:    
    # get a copy of the phase weights
    mfptRecalc = np.array(summary.weights)
    
    # invert all of the weights aside from the zeroth
    mfptRecalc[1:] = 1/mfptRecalc[1:]
    
    # now take the cumulative product accross all of the phase weights
    mfptRecalc[...] = np.cumprod(mfptRecalc)
    
    mfptRecalcs.append(mfptRecalc)