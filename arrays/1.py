from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            want = target - nums[i]
            if want in d:
                return [d[want], i]
            d[nums[i]] = i
        return []

def test_example_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_example_2():
    result = Solution().twoSum([3, 2, 4], 6)
    assert result == [1, 2]

def test_example_3():
    assert Solution().twoSum([3, 3], 6) == [0, 1]

def test_negative_numbers():
    result = Solution().twoSum([1, -2, 5, 10], -1)
    assert result == [0, 1] or result == [1, 0]

def test_large_array():
    assert Solution().twoSum([1, 4, 10, -3], 14) == [1, 2] or Solution().twoSum([1, 4, 10, -3], 14) == [2, 1]

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_negative_numbers()
    test_large_array()
    print("All tests passed.")
