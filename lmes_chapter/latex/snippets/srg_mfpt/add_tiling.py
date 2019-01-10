import h5py

with h5py.File('data/srg.lm') as f:
    # remove any existing Tilings group
    if 'Tilings' in f.keys():
        del f['Tilings']
    
    # create the Tilings group
    tilings = f.create_group('Tilings')
    
    # add the subgroup for tiling 0
    tiling0 = tilings.create_group('0')
    
    # set this tiling's ID to 0, its OrderParameterID to 0, and its Type to 0
    tiling0.attrs['ID'] = 0
    tiling0.attrs['OrderParameterID'] = 0
    tiling0.attrs['Type'] = 0
    
    # add the Basins. There is 1 chemical species in this model, and we are 
    # going to set 2 initial basins, so Basins will be a 2 x 1 array
    basins = np.zeros((2,1), dtype=int)
    basins[0,0] = 10
    basins[1,0] = 160
    tiling0.create_dataset('Basins', data=basins)
    
    # add the Edges
    edges = np.linspace(23.0, 150.0, num=13)
    tiling0.create_dataset('Edges', data=edges)