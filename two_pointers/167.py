from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return []


def test_example_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]

def test_example_2():
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]

def test_example_3():
    assert Solution().twoSum([-1, 0], -1) == [1, 2]

def test_negative_numbers():
    assert Solution().twoSum([-3, -1, 0, 2], -1) == [1, 4]

def test_two_elements():
    assert Solution().twoSum([1, 2], 3) == [1, 2]

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_negative_numbers()
    test_two_elements()
    print("All tests passed.")
