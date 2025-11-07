from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        m = 0

        while left < right:
            sum = min(height[left], height[right]) * (right - left)
            m = max(m, sum)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return m


def test_example_1():
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_example_2():
    assert Solution().maxArea([1,1]) == 1

def test_two_tall_lines():
    assert Solution().maxArea([4,3,2,1,4]) == 16

def test_increasing_heights():
    assert Solution().maxArea([1,2,3,4,5]) == 6

def test_all_same():
    assert Solution().maxArea([2,2,2,2]) == 6

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_two_tall_lines()
    test_increasing_heights()
    test_all_same()
    print("All tests passed.")
