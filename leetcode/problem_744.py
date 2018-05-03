'''
744. Find Smallest Letter Greater Than Target
'''

from unittest import TestCase

class FindSmallestTest(TestCase):
    def test_one_edge_case(self):
        letters = ["c","f","j"]
        target = "a"
        f = FindSmallest(letters, target)
        self.assertEquals(f,"c")


class FindSmallest:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def binary_search(self):
        arr = self.arr
        target = self.target
        array_length = len(arr)
        if array_length < 1:
            return None
        left = 0
        right = array_length-1
        while (left <= right):
            mid = left + (right-left)/2
            if arr[mid] < target and mid == left:
                return arr[mid]
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return arr[mid]

letters = ["c","f","j"]
target = "c"
f = FindSmallest(letters, target)
assert f.binary_search() == "f"