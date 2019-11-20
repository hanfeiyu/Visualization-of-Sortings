#
# Authors: Kenneth, Hanfei Yu
#

# Python program for implementation of Quicksort Sort 

import copy as cp
from Parameters.parameters import dataset_size


# Function for wrapping up the _quickSort()
def quickSort(dataset):
    
    # Add the first frame
    frames = [dataset]
    dataset_cp = cp.deepcopy(dataset)

    _quickSort(dataset_cp, 0, dataset_size-1, frames)
    
    # Set all bars to lightgreen once sorting finished
    frames.append(dataset_cp)
    for i in range(dataset_size):
        frames[-1][i].setColor('lightgreen')

    return frames

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(dataset, low, high, frames):
    i = (low - 1) # index of smaller element
    pivot = dataset[high].value # pivot
    
    for j in range(low, high):
        
        # Scan from low index, set scanner and pivot to yellow
        frames.append(cp.deepcopy(dataset))
        frames[-1][j].setColor('yellow')
        frames[-1][high].setColor('yellow')

        # If current element is smaller than the pivot 
        if dataset[j].value < pivot: 
 
            # Increment index of smaller element 
            i = i+1

            # Before swap, add one frame
            frames.append(cp.deepcopy(dataset))
            frames[-1][i+1].setColor('red')
            frames[-1][j].setColor('red')
            frames[-1][high].setColor('yellow')
            
            # Swap
            dataset[i], dataset[j] = dataset[j], dataset[i] 
            
            # After swap, add one frame
            frames.append(cp.deepcopy(dataset))
            frames[-1][i].setColor('green')
            frames[-1][j].setColor('green')
            frames[-1][high].setColor('yellow')
    
    # Before swap, add one frame
    frames.append(cp.deepcopy(dataset))
    frames[-1][i+1].setColor('red')
    frames[-1][high].setColor('red')
    frames[-1][high].setColor('yellow')
    
    dataset[i+1], dataset[high] = dataset[high], dataset[i+1]

    # After swap, add one frame
    frames.append(cp.deepcopy(dataset))
    frames[-1][i+1].setColor('green')
    frames[-1][high].setColor('green')
    frames[-1][high].setColor('yellow')
    frames[-1][i+1].setColor('lightgreen')

    return (i+1) 

# The main function that implements QuickSort 
# Function to do Quick sort 
def _quickSort(dataset, low, high, frames):
    if low < high:
        
        # pi is partitioning index, arr[p] is now 
        # at right place
        pi = partition(dataset, low, high, frames) 
            
        # Separately sort elements before
        # partition and after partition
        _quickSort(dataset, low, pi-1, frames)
        _quickSort(dataset, pi+1, high, frames) 

        
