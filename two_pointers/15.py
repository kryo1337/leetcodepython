from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtr = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                sum = nums[left] + nums[right]

                if sum == target:
                    rtr.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif sum < target:
                    left += 1
                else:
                    right -= 1

        return rtr

def test_example_1():
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result) == sorted(expected)

def test_example_2():
    assert Solution().threeSum([0, 1, 1]) == []

def test_example_3():
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]

def test_empty_array():
    assert Solution().threeSum([]) == []

def test_single_element():
    assert Solution().threeSum([0]) == []

def test_two_elements():
    assert Solution().threeSum([0, 0]) == []

def test_multiple_triplets():
    result = Solution().threeSum([-2, 0, 0, 2, 2])
    expected = [[-2, 0, 2]]
    assert sorted(result) == sorted(expected)

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_empty_array()
    test_single_element()
    test_two_elements()
    test_multiple_triplets()
    print("All tests passed.")
