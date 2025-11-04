from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0

        for num in s:
            if num - 1 not in s:
                curr = num
                len = 1
                while curr + 1 in s:
                    curr += 1
                    len += 1
                m = max(m, len)

        return m


def test_example_1():
    assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4

def test_example_2():
    assert Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

def test_empty_array():
    assert Solution().longestConsecutive([]) == 0

def test_single_element():
    assert Solution().longestConsecutive([1]) == 1

def test_no_consecutive():
    assert Solution().longestConsecutive([1,3,5,7,9]) == 1

def test_duplicates():
    assert Solution().longestConsecutive([1,2,0,1]) == 3

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_empty_array()
    test_single_element()
    test_no_consecutive()
    test_duplicates()
    print("All tests passed.")
