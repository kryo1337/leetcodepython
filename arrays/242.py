class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            count = d.get(c, 0)
            if count == 0:
                return False
            d[c] = count - 1

        return True

def test_valid_anagram():
    assert Solution().isAnagram("anagram", "nagaram") == True

def test_not_anagram():
    assert Solution().isAnagram("rat", "car") == False

def test_empty_strings():
    assert Solution().isAnagram("", "") == True

def test_different_lengths():
    assert Solution().isAnagram("a", "ab") == False

if __name__ == "__main__":
    test_valid_anagram()
    test_not_anagram()
    test_empty_strings()
    test_different_lengths()
    print("All tests passed.")
