#
# Authors: Kenneth, Hanfei Yu
#

import copy as cp
from Parameters.parameters import dataset_size


def bubbleSort(dataset):

    # Add the first frame
    frames = [dataset]
    dataset_cp = cp.deepcopy(dataset)

	# Traverse through all array elements
    for i in range(dataset_size):

	# Last i elements are already in place
    	for j in range(0, dataset_size-i-1):

		# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
            if dataset_cp[j].value > dataset_cp[j+1].value :
                
                # Before swap, add one frame
                frames.append(cp.deepcopy(dataset_cp))
                frames[-1][j].setColor('red')
                frames[-1][j+1].setColor('red')

                # Swap
                dataset_cp[j], dataset_cp[j+1] = dataset_cp[j+1], dataset_cp[j]
                
                # After swap, add one frame
                frames.append(cp.deepcopy(dataset_cp))
                frames[-1][j].setColor('green')
                frames[-1][j+1].setColor('green')
            else:
                # Else add one frame
                frames.append(cp.deepcopy(dataset_cp))
                frames[-1][j].setColor('green')
                frames[-1][j+1].setColor('green')

    # Set all to green once sorting finished and add one frame
    frames.append(dataset_cp)
    
    for i in range(dataset_size):
        frames[-1][i].setColor('lightgreen')
    
    return frames
