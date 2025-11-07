from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        left_m = height[left]
        right_m = height[right]

        while left < right:
            if left_m < right_m:
                left += 1
                left_m = max(left_m, height[left])
                water += left_m - height[left]
            else:
                right -= 1
                right_m = max(right_m, height[right])
                water += right_m - height[right]

        return water


def test_example_1():
    assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_example_2():
    assert Solution().trap([4,2,0,3,2,5]) == 9

def test_no_water():
    assert Solution().trap([3,2,1]) == 0

def test_flat():
    assert Solution().trap([1,1,1,1]) == 0

def test_two_bars():
    assert Solution().trap([3,0,3]) == 3

def test_single_bar():
    assert Solution().trap([5]) == 0

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_no_water()
    test_flat()
    test_two_bars()
    test_single_bar()
    print("All tests passed.")
