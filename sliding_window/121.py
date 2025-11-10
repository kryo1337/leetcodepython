from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minik = prices[0]
        maxik = 0

        for i in range(1, len(prices)):
            profit = prices[i] - minik
            maxik = max(maxik, profit)
            minik = min(minik, prices[i])

        return maxik


def test_example_1():
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5

def test_example_2():
    assert Solution().maxProfit([7,6,4,3,1]) == 0

def test_example_3():
    assert Solution().maxProfit([1,2,3,4,5]) == 4

def test_single_day():
    assert Solution().maxProfit([5]) == 0

def test_two_days():
    assert Solution().maxProfit([7,1]) == 0

def test_increasing_then_decreasing():
    assert Solution().maxProfit([1,3,2,4,1]) == 3

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_single_day()
    test_two_days()
    test_increasing_then_decreasing()
    print("All tests passed.")
