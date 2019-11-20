#
# Authors: Kenneth, Hanfei Yu
#

import copy as cp
from Parameters.parameters import dataset_size

# Python program for implementation of Selection 
# Sort 

def selectionSort(dataset): 
    # Add the first frame
    frames = [dataset]
    dataset_cp = cp.deepcopy(dataset)

    # Traverse through all array elements 
    for i in range(dataset_size): 
    	
    	# Find the minimum element in remaining 
    	# unsorted array
        min_idx = i
        for j in range(i+1, dataset_size):
            
            # Scan the dataset with yellow bar, minimum bar left red
            frames.append(cp.deepcopy(dataset_cp))
            frames[-1][min_idx].setColor('red')
            frames[-1][j].setColor('yellow')
            
            if dataset_cp[min_idx].value > dataset_cp[j].value:
                
                # Find new minimum bar, set its color to red
                frames.append(cp.deepcopy(dataset_cp))
                frames[-1][j].setColor('red')
                
                min_idx = j 

        # Swap the found minimum element with 
        # the first element

        # Before swap, add one frame
        frames.append(cp.deepcopy(dataset_cp))
        frames[-1][i].setColor('red')
        frames[-1][min_idx].setColor('red')
        
        # Swap
        dataset_cp[i], dataset_cp[min_idx] = dataset_cp[min_idx], dataset_cp[i] 
    
        # After swap, add one frame
        frames.append(cp.deepcopy(dataset_cp))
        frames[-1][i].setColor('green')
        frames[-1][min_idx].setColor('green')

    # Set all to green once sorting finished and add one frame
    frames.append(dataset_cp)

    for i in range(dataset_size):
        frames[-1][i].setColor('lightgreen')

    return frames

