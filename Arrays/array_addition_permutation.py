"""
Have the function ArrayAddition(arr) take the array of numbers stored in arr and return True if any combination
of numbers in the array(excluding the largest number) can be added up to equal the largest number in the array,
Otherwise return False.

For example: If arr contains [4, 6, 23, 10, 1, 3] the output should return True because 4 + 6 + 10 + 3 = 23

The array will not be empty, will not contain all the same elements and may contain negative numbers.

Examples:

Input: [5, 7, 16, 1, 2]
Output: False

Input: [3, 5, -1, 8, 12]
Output: True
"""
import unittest
from typing import List


def array_addition(arr: List[int]) -> bool:
    meets = False
    largest = max(arr)

    arr.remove(largest)

    permutations = permutation(arr)

    for perm in permutations:
        prefix_sums_arr = prefix_sums(perm)

        for h in range(len(perm)):
            for j in range(h, len(perm)):
                total = count_total(prefix_sums_arr, h, j)

                if total == largest:
                    return True

                if total > largest:
                    continue

    return meets


def permutation(lst):
    """
    Python function to print permutations of a given list

    :param lst:
    :return:
    """
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are more than 1 characters

    permutation_lst = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is remaining list
        rem_lst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first element
        for p in permutation(rem_lst):
            permutation_lst.append([m] + p)
    return permutation_lst


def prefix_sums(arr: List[int]):
    """
    The array returned here is one element larger than the original

    :param arr:
    :return:
    """
    n = len(arr)
    P = [0] * (n + 1)

    for k in range(1, n + 1):
        P[k] = P[k - 1] + arr[k - 1]

    return P


def count_total(P, x, y):
    """

    :param P: a Prefix sum array
    :param x:
    :param y:
    :return:
    """
    return P[y + 1] - P[x]


class TestStringMethods(unittest.TestCase):
    arr1, meets1 = [4, 6, 23, 10, 1, 3], True
    arr2, meets2 = [5, 7, 16, 1, 2], False
    arr3, meets3 = [3, 5, -1, 8, 12], True
    arr4, meets4 = [4, 7, 11, 10, 2, 3], True

    def test_array_addition(self):
        self.assertEqual(array_addition(self.arr1), self.meets1)
        self.assertEqual(array_addition(self.arr2), self.meets2)
        self.assertEqual(array_addition(self.arr3), self.meets3)
        self.assertEqual(array_addition(self.arr4), self.meets4)


if __name__ == '__main__':
    unittest.main()
