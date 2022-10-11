import unittest
import random


def sort(array: list) -> list:
    """Sort array with quicksort

    Args:
        array (list): input array

    Returns:
        list: sorted array
    """
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot_index = random.randint(0, len(array) - 1)
        pivot = array[pivot_index]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    return array


class TestSort(unittest.TestCase):
    def test_task(self):
        arr = [-5, -23, 5, 0, 23, -6, 23, 67]
        expected = [-23, -6, -5, 0, 5, 23, 23, 67]
        self.assertEqual(sort(arr), expected)

    def test_one_elem(self):
        arr = expected = [0]
        self.assertEqual(sort(arr), expected)

    def test_same_elems(self):
        arr = expected = [1, 1, 1, 1, 1, 1]
        self.assertEqual(sort(arr), expected)

    def test_dupes(self):
        arr = [3, 3, 1, 1, 2, 2]
        expected = [1, 1, 2, 2, 3, 3]
        self.assertEqual(sort(arr), expected)

    def test_empty(self):
        arr = expected = []
        self.assertEqual(sort(arr), expected)


def main():
    arr = [-5, -23, 5, 0, 23, -6, 23, 67]
    print(sort(arr))


if __name__ == "__main__":
    unittest.main()
