import h5py

with h5py.File('data/gts.lm') as f:
    # remove any existing OrderParameters group
    if 'OrderParameters' in f.keys():
        del f['OrderParameters']
    
    # create the OrderParameters group
    oparams = f.create_group('OrderParameters')
    
    # add the subgroup for order parameter 0
    oparam0 = oparams.create_group('0')
    
    # set this order parameter's ID to 0, and its Type to 0
    oparam0.attrs['ID'] = 0
    oparam0.attrs['Type'] = 0
    
    # add the SpeciesIDs. This array should always be of type `int`
    speciesIDs = np.array([0, 1, 2, 3, 4, 5], dtype=int)
    oparam0.create_dataset('SpeciesIDs', data=speciesIDs)
    
    # add the SpeciesCoefficients. This array should always be of type `float`
    speciesCoefficients = np.array([-1, -2, -2, 1, 2, 2], dtype=float)
    oparam0.create_dataset('SpeciesCoefficients', data=speciesCoefficients)