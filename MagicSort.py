import math
from random import randrange

def linear_scan(L):
    '''
    returns the most efficient sorting algorithm given a list of integers
    '''

    if len(L) == 1:
        return 'List only has 1 item'
    elif len(L) == 0:
        return 'List is empty'

    flag = 0
    i = 1
    while i < len(L):
        if(L[i] < L[i - 1]):
            flag = 1
        i += 1
    if (not flag):
        return "sorted"
    
    
    L2 = sorted(L, reverse=True)
    if L == L2:
        return 'reverse list' #if the list is reverse sorted

    j = 0
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            j += 1  
    if j <= 5:
        return 'insertion sort' #if 5 or less items are out of place

    else:
        return 'quicksort' #if all 3 base cases fail



def reverse_list(L):
    '''
    reverses list in linear time 
    '''

    # Initialize two pointers, one at the beginning and one at the end of the list
    left = 0
    right = len(L) - 1
    
    # Swap elements at the two pointers until they meet in the middle
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1



def insertionsort(L, left = 0, right = None):
    '''
    sorts list using insertion sort algorithim 
    '''
    
    if right is None:
        right = len(L) - 1 

    for i in range(left + 1, right + 1):
        key = L[i]
        j = i - 1
        while j >= left and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key



def quicksort(L, left = 0, right = None, depth=None):
    '''
    sorts list using quicksort algorithim
    '''

    if right == None:
        right = len(L) - 1

    if left >= right:
        return

    if right - left <= 16:
        insertionsort(L, left, right)
        return
    
    if depth is None:
        # If no maximum depth is provided, use math.log2(n)+1 as the best-case maximum depth
        depth = int(math.log2(right - left + 1) + 1)

    if depth == 0:
        mergesort(L, left, right)
        return
    
    pivot_index = right
    pivot_val = L[pivot_index]

    # Partition the sublist around the pivot
    i = left - 1
    for j in range(left, right):
        if L[j] <= pivot_val:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[pivot_index] = L[pivot_index], L[i+1]

    # Recursively sort the two partitions
    quicksort(L, left, i, depth-1)
    quicksort(L, i+2, right, depth-1)



def mergesort(L, left = 0, right = None):
    '''
    sorts list using mergesort algorithm 
    '''

    if right is None:
        right = len(L)

    # Base Case!
    if len(L) < 2:
        return 
    
    # Divide!
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]

    # Conquer!
    mergesort(A)
    mergesort(B)

    # Combine!
    merge(A, B, L)

def merge(A, B, L):
    '''
    merges the seperately sorted sublists
    '''
    i = 0 # index into A
    j = 0 # index into B
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i = i + 1
        else:
            L[i+j] = B[j]
            j = j + 1
    # Add any remaining elements once one list is empty
    L[i+j:] = A[i:] + B[j:]


   
def magic_sort(L):
    '''
    sorts list in-place using most efficient sorting algorithms, 
    returns a set of which algo's are used
    '''
    s = set()
    x = linear_scan(L)

    if x == 'sorted':
        s.add('sorted')

    elif x == 'reverse list':
        s.add('reverse list')
        reverse_list(L)

    elif x == 'insertion sort':
        s.add('insertion sort')
        insertionsort(L)

    elif x == 'quicksort':
        depth = math.ceil(math.log2(len(L))) + 1
        quicksort(L, 0, len(L)-1, depth)
        s.add('quicksort')
        s.add('insertion sort') #since if it is quick sorting it will use insertion sort
        if depth <= 2 * (math.ceil(math.log2(len(L))) + 1):
            mergesort(L, 0, len(L)-1)
            s.add('mergesort')

    return s
