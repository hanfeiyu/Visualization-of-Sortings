#
# Authors: Kenneth, Hanfei Yu
#

import copy as cp
from Parameters.parameters import dataset_size
 

# Function to do insertion sort 
def insertionSort(dataset): 
    
    # Add the first frame
    frames = [dataset]
    dataset_cp = cp.deepcopy(dataset)

    # Traverse through 1 to len(arr) 
    for i in range(1, dataset_size): 
   
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        for j in range(i, 0, -1):
            
            if dataset_cp[j-1].value > dataset_cp[j].value:

                # Before swap, add one frame
                frames.append(cp.deepcopy(dataset_cp))
                frames[-1][j].setColor('red')
                frames[-1][j-1].setColor('red')
                
                # Swap
                dataset_cp[j-1], dataset_cp[j] = dataset_cp[j], dataset_cp[j-1] 

                # After swap, add one frame
                frames.append(cp.deepcopy(dataset_cp))
                frames[-1][j].setColor('green')
                frames[-1][j-1].setColor('green')
            else:
                # Else add one frame and break
                frames.append(cp.deepcopy(dataset_cp))
                frames[-1][j].setColor('green')
                frames[-1][j-1].setColor('green')
                break
    
    # Set all to green once sorting finished and add one frame
    frames.append(dataset_cp)
    
    for i in range(dataset_size):
        frames[-1][i].setColor('lightgreen')

    return frames
    
    
  
