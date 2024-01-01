import unittest
import random
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


class Test_linear_scan(unittest.TestCase):
    def test_linear_scan(self):
        '''
        tests functionality of the linear_scan function
        '''
        L = [1, 2, 3, 4, 5]
        self.assertEqual(linear_scan(L), 'sorted')

        L2 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]
        self.assertEqual(linear_scan(L2), 'insertion sort')

        L3 = [5, 4, 3, 2, 1]
        self.assertEqual(linear_scan(L3), 'reverse list')

class Test_reverse_list(unittest.TestCase):
    def test_reverse_list(self):
        '''
        tests functionality of reverse_list function
        '''
        L = [1, 2, 3, 4, 5]
        reverse_list(L)
        self.assertEqual(L, [5, 4, 3, 2, 1])

class Test_insertionsort(unittest.TestCase):
    def test_insertion_sort(self):
        '''
        tests functionality of insertionsort function
        '''
        L = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]
        insertionsort(L)
        self.assertEqual(L, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

class Test_quicksort(unittest.TestCase):
    def test_quick_sort(self):
        '''
        tests functionality of quicksort function
        '''
        L = []
        for i in range(5):
            for i in range(100):
                L.append(i)
        random.shuffle(L)
        y = sorted(L)
        quicksort(L)
        self.assertEqual(L, y)

        #tests functionality of the "<= 16 items in a list" base case 
        #when the list is passed into quick sort to make sure  it uses insertionsort 
        L2 = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
        quicksort(L2)
        self.assertEqual(L2, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

        #tests functionality of the "recursive depth" base case inside quicksort
        #by making sure the list gets sorted with mergesort if the recursive depth reaches twice or
        #more the best-case maximum depth. Does this by making the pivot point a terrible spot to be like 
        #a reverse sorted list since the pivots always the last number
        L = []
        for i in range(5):
            for i in range(100):
                L.append(i)
        L.reverse()
        y = sorted(L)
        quicksort(L)
        self.assertEqual(L, y)

class Test_mergesort(unittest.TestCase):
    def test_mergesort(self):
        '''
        tests functionality of mergesort function
        '''
        L = []
        for i in range(5):
            for i in range(100):
                L.append(i)
        random.shuffle(L)
        y = sorted(L)
        mergesort(L)
        self.assertEqual(L, y)

class Test_magicsort(unittest.TestCase):
    def test_magicsort(self):
        '''
        tests functionality of magic sort function
        '''
        #tests sorted list base case
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(magic_sort(L), {'sorted'})
        self.assertEqual(L, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        #tests reverse sorted list base case
        L2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(magic_sort(L2), {'reverse list'})
        self.assertEqual(L2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        #tests insertion sort base case
        L3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]
        self.assertEqual(magic_sort(L3), {'insertion sort'})
        self.assertEqual(L3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        #tests quick sort to see if it tracks merge and insertion being called
        n = int(1E5)
        L5 = [(n-i) for i in range(n)]
        L5[:6] = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(magic_sort(L5), {'quicksort', 'insertion sort', 'mergesort'})

unittest.main()