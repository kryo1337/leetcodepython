from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for str in strs:
            key = tuple(sorted(str))
            if key not in d:
                d[key] = []
            d[key].append(str)
        return list(d.values())


def test_example_1():
    result = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    result_sorted = [sorted(group) for group in result]
    expected = [sorted(group) for group in [["eat","tea","ate"],["tan","nat"],["bat"]]]
    assert sorted(result_sorted) == sorted(expected)

def test_example_2():
    assert Solution().groupAnagrams([""]) == [[""]]

def test_example_3():
    assert Solution().groupAnagrams(["a"]) == [["a"]]

def test_no_anagrams():
    result = Solution().groupAnagrams(["abc", "def", "ghi"])
    assert len(result) == 3

def test_all_anagrams():
    result = Solution().groupAnagrams(["abc", "bca", "cab"])
    assert len(result) == 1
    assert len(result[0]) == 3

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_no_anagrams()
    test_all_anagrams()
    print("All tests passed.")
