from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for n in nums:
            if n in d:
                return True
            d[n] = 1
        return False

def test_example_1():
    assert Solution().containsDuplicate([1, 2, 3, 1]) == True

def test_example_2():
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False

def test_example_3():
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

def test_single_element():
    assert Solution().containsDuplicate([1]) == False

def test_two_duplicates():
    assert Solution().containsDuplicate([5,5]) == True

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_single_element()
    test_two_duplicates()
    print("All tests passed.")
