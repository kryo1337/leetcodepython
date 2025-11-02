from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rtr = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            rtr[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            rtr[i] *= right
            right *= nums[i]

        return rtr

def test_example_1():
    assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]

def test_example_2():
    assert Solution().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

def test_two_elements():
    assert Solution().productExceptSelf([2,3]) == [3,2]

def test_with_negative():
    assert Solution().productExceptSelf([-1,-2,-3]) == [6,3,2]

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_two_elements()
    test_with_negative()
    print("All tests passed.")
