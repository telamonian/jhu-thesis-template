import h5py

with h5py.File('data/srg.lm') as f:
    # NB: convert any numerical types to strings before setting option values
    
    # the trajectory state output writing interval (in terms of the 
    # internal simulation time).
    f['Parameters'].attrs['writeInterval'] = str(1.0)
    
    # we'll need some information from the StageOutputRaw record in order 
    # to calculate the landscape
    f['Parameters'].attrs['ffluxStageOutputRaw'] = 'True'
    
    # set an error goal, which controls the overall accuracy of 
    # the simulation. Defaults to .05
    f['Parameters'].attrs['errorGoal'] = str(.10)