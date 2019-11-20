#
# Author: Hanfei Yu
#

import random as rd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as anime
import sys

from SortingTechs.Bubble_Sort import bubbleSort
from SortingTechs.Selection_Sort import selectionSort
from SortingTechs.Insertion_Sort import insertionSort
from SortingTechs.Quick_Sort import quickSort
from SortingTechs.Merge_Sort import mergeSort
 
from Parameters.parameters import *


# Initialize sorting list
sorting_techs = [bubbleSort, selectionSort, insertionSort, quickSort, mergeSort]

# Create original dataset
def createOriginalDataset(data_type):
    dataset = []

    if data_type == '1': # Random dataset
        dataset = list(range(1, dataset_size + 1))
        rd.shuffle(dataset)

    elif data_type == '2': # Sorted dataset
        dataset = list(range(1, dataset_size + 1))

    elif data_type == '3': # Reserved dataset
        dataset = list(range(dataset_size + 1, 1, -1))

    elif data_type == '4': # Almost-sorted dataset
        dataset = list(range(1, dataset_size + 1))
        x = rd.randint(0, dataset_size - 1)
        y = rd.randint(0, dataset_size - 1)

        while x == y:
            y = rd.randint(0, dataset_size - 1)

        dataset[x], dataset[y] = dataset[y], dataset[x]

    elif data_type == '5': # Almost-reversed dataset
        dataset = list(range(dataset_size, 0, -1))
        x = rd.randint(0, dataset_size - 1)
        y = rd.randint(0, dataset_size - 1)

        while x == y:
            y = rd.randint(0, dataset_size - 1)
        
        dataset[x], dataset[y] = dataset[y], dataset[x]
    
    print(dataset)

    return dataset

# Draw all the figures of five sorting techs
def drawAllFigures(dataset, data_type):
    
    # Prepare the elemental setup for figure
    axis = []
    frames_all = []
    figure = plt.figure(1, figsize=(16, 9))
    data_class = [data(d) for d in dataset]

    for i in range(5):
        axis.append(figure.add_subplot(334 + i))
        axis[-1].set_xticks([])
        axis[-1].set_yticks([])

    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95, wspace=0.1, hspace=0.2)
    
    # Retrieve the frames
    for i in range(5):
        frames_all.append(sorting_techs[i](data_class))

    # Make animation
    def KyoAni(frame_num):
        bars = []
        
        if data_type == '1':
            figure.suptitle('Random Dataset', fontsize='xx-large', fontweight='heavy', bbox=dict(edgecolor='blue', alpha=0.65))
        elif data_type == '2':
            figure.suptitle('Sorted Dataset', fontsize='xx-large', fontweight='heavy', bbox=dict(edgecolor='blue', alpha=0.65))
        elif data_type == '3':
            figure.suptitle('Reversed Dataset', fontsize='xx-large', fontweight='heavy', bbox=dict(edgecolor='blue', alpha=0.65))
        elif data_type == '4':
            figure.suptitle('Almost-sorted Dataset', fontsize='xx-large', fontweight='heavy', bbox=dict(edgecolor='blue', alpha=0.65))
        elif data_type == '5':
            figure.suptitle('Almost-reversed Dataset', fontsize='xx-large', fontweight='heavy', bbox=dict(edgecolor='blue', alpha=0.65))

        for i in range(5):
            if len(frames_all[i]) > frame_num:
                axis[i].cla()
                axis[i].set_title(titles[i])
                axis[i].set_xticks([])
                axis[i].set_yticks([])

                bars = bars + axis[i].bar(list(range(dataset_size)), [d.value for d in frames_all[i][frame_num]], 1, color = [d.color for d in frames_all[i][frame_num]]).get_children()

        return bars

    # Call KyoAni
    KyotoAnime = anime.FuncAnimation(figure, KyoAni, frames = max(len(frame) for frame in frames_all), interval = frame_interval)

    return plt, KyotoAnime

    
# Main function
if __name__ == "__main__":
        
    data_type = '1' # By default
        
    if len(sys.argv) > 1:
        data_type = sys.argv[1]
        
        if data_type == '1':
            print("Now generating the output of random dataset: \n")
        elif data_type == '2':
            print("Now generating the output of sorted dataset: \n")
        elif data_type == '3':
            print("Now generating the output of reversed dataset: \n")
        elif data_type == '4':
            print("Now generating the output of almost-sorted dataset: \n")
        elif data_type == '5':
            print("Now generating the output of almost-reversed dataset: \n")
        else:
            print('Invalid data!')
            exit()
        
    dataset = createOriginalDataset(data_type)
    plt, _ = drawAllFigures(dataset, data_type)
    plt.show()


