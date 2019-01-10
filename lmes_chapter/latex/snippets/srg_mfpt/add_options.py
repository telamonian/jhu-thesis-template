import h5py

with h5py.File('data/srg.lm') as f:
    # NB: convert all option values to str before setting them
    
    # turn on output of pilot stage data
    f['Parameters'].attrs['ffluxPilotOutput'] = str(True)
    
    # set a target error goal for the simulation as a whole. Defaults to .05
    f['Parameters'].attrs['errorGoal'] = str(.10)