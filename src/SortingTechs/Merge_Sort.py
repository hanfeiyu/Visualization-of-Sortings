#
# Author: Kenneth, Hanfei Yu
#

import copy as cp
from Parameters.parameters import dataset_size


def mergeSort(dataset):

    # Add the first frame
    frames = [dataset]
    dataset_cp_1 = cp.deepcopy(dataset)
    dataset_cp_2 = cp.deepcopy(dataset)

    _mergeSort(dataset_cp_1, dataset_cp_2, frames)

    # Set all bars to lightgreen once sorting finished and add one frame
    frames.append(dataset_cp_2)

    for i in range(dataset_size):
        frames[-1][i].setColor('lightgreen')

    return frames

def _mergeSort(dataset, dataset_cp, frames):

    if len(dataset) > 1:
       mid = len(dataset) // 2
       lefthalf = dataset[:mid]
       righthalf = dataset[mid:]

       #recursion
       _mergeSort(lefthalf, dataset_cp, frames)
       _mergeSort(righthalf, dataset_cp, frames)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i].value < righthalf[j].value:
               dataset[k] = lefthalf[i]
               
               # Before copy, add one frame
               frames.append(cp.deepcopy(dataset_cp))
               frames[-1][k].setColor('red')

               # Cpoy
               dataset_cp[k] =lefthalf[i]

               # After copy, add one frame
               frames.append(cp.deepcopy(dataset_cp))
               frames[-1][k].setColor('green')
                
               i = i+1
           else:
               dataset[k] = righthalf[j]
            
               # Before copy, add one frame
               frames.append(cp.deepcopy(dataset_cp))
               frames[-1][k].setColor('red')

               # Cpoy
               dataset_cp[k] =righthalf[j]

               # After copy, add one frame
               frames.append(cp.deepcopy(dataset_cp))
               frames[-1][k].setColor('green')
               
               j = j+1
           
           k = k+1

       while i < len(lefthalf):
           dataset[k] = lefthalf[i]
           
           # Before copy, add one frame
           frames.append(cp.deepcopy(dataset_cp))
           frames[-1][k].setColor('red')
           
           # Cpoy
           dataset_cp[k] =lefthalf[i]
           
           # After copy, add one frame
           frames.append(cp.deepcopy(dataset_cp))
           frames[-1][k].setColor('green')
           
           i = i+1
           k = k+1

       while j < len(righthalf):
           dataset[k] = righthalf[j]
           
           # Before copy, add one frame
           frames.append(cp.deepcopy(dataset_cp))
           frames[-1][k].setColor('red')
           
           # Cpoy
           dataset_cp[k] =righthalf[j]
           
           # After copy, add one frame
           frames.append(cp.deepcopy(dataset_cp))
           frames[-1][k].setColor('green')
           
           j=j+1
           k=k+1
