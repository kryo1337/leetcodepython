class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = dict()
        left = 0
        freq = 0
        maxik = 0

        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0) + 1
            freq = max(freq, d[s[right]])
            while left <= right and (right - left + 1 - freq > k):
                d[s[left]] = d.get(s[left], 0) - 1
                if d[s[left]] == 0:
                    del d[s[left]]
                freq = max(d.values()) if d else 0
                left += 1

            maxik = max(maxik, right - left + 1)

        return maxik


def test_example_1():
    assert Solution().characterReplacement("ABAB", 2) == 4

def test_example_2():
    assert Solution().characterReplacement("AABABBA", 1) == 4

def test_example_3():
    assert Solution().characterReplacement("ABBB", 0) == 3

def test_empty_string():
    assert Solution().characterReplacement("", 0) == 0

def test_all_same_chars():
    assert Solution().characterReplacement("AAAA", 2) == 4

def test_alternating():
    assert Solution().characterReplacement("ABABAB", 1) == 3

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_empty_string()
    test_all_same_chars()
    test_alternating()
    print("All tests passed.")
