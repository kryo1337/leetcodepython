from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for n in nums:
            d[n] = d.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in d.items():
            bucket[freq].append(num)

        rtr = []
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                rtr.append(num)
                if len(rtr) == k:
                    return rtr

        return rtr


def test_example_1():
    result = Solution().topKFrequent([1,1,1,2,2,3], 2)
    assert sorted(result) == [1, 2]

def test_example_2():
    assert Solution().topKFrequent([1], 1) == [1]

def test_all_same():
    result = Solution().topKFrequent([4,4,4,4], 1)
    assert result == [4]

def test_multiple_frequencies():
    result = Solution().topKFrequent([1,2,2,3,3,3], 2)
    assert sorted(result) == [2, 3]

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_all_same()
    test_multiple_frequencies()
    print("All tests passed.")
