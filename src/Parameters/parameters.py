#
# Author: Hanfei Yu
# Set up parameters for visualization
#


# Initialize figure title list
titles = [r'Bubble Sort ($O(n^2)$)', r'Selection Sort ($O(n^2)$)', r'Insertion Sort ($O(n^2)$)', r'Quick Sort ($O(nlogn)$)', r'Merge Sort ($O(nlogn)$)']

# Initialize statement list
statement = ['''For the random dataset in our experiment, 
            Quick Sort was the fastest and followed by Merge Sort, Insertion Sort, Selection Sort and then Bubble Sort.
            This is according to the average running times as specified.''', 
            '''For the sorted dataset in our experiment, 
            the Insertion Sort was the fastest and followed by Merge Sort, Bubble Sort, Selection Sort and then Quick Sort. 
            This is in accordance with the best running times as specified.''', 
            '''For the reversed dataset, 
            Merge Sort was the fastest and followed by Selection Sort, Insertion Sort, Bubble Sort and then Quick Sort. 
            This is almost in accordance with the worse running times as specified.''', 
            '''For the almost-sorted dataset, 
            Insertion Sort was the fastest and followed by Merge Sort, Bubble Sort, Selection Sort and then Quick Sort. 
            This is also almost in accordance with the good or best running times of the sorting algorithms.''', 
            'For almost-reversed dataset',]

# Initialize parameters
dataset_size = 32
frame_interval = 1

# Define class 'data'
class data:

    def __init__(self, value):
        self.value = value
        self.color = self.setColor()

    def setColor(self, rgba = None):
        if rgba == None:
            rgba = 'blue'

        self.color = rgba

        return rgba
