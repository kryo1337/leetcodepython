class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        left = 0
        maxik = 0

        for right in range(len(s)):
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1

            d[s[right]] = right

            curr = right - left + 1
            maxik = max(maxik, curr)

        return maxik

def test_example_1():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

def test_example_2():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

def test_example_3():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3

def test_empty_string():
    assert Solution().lengthOfLongestSubstring("") == 0

def test_single_character():
    assert Solution().lengthOfLongestSubstring("a") == 1

def test_all_unique():
    assert Solution().lengthOfLongestSubstring("abcde") == 5

def test_with_numbers():
    assert Solution().lengthOfLongestSubstring("abc123def") == 9

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_empty_string()
    test_single_character()
    test_all_unique()
    test_with_numbers()
    print("All tests passed.")
