class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

def test_example_1():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True

def test_example_2():
    assert Solution().isPalindrome("race a car") == False

def test_empty_after_filter():
    assert Solution().isPalindrome(" ") == True

def test_all_special_chars():
    assert Solution().isPalindrome(".,") == True

def test_single_char():
    assert Solution().isPalindrome("a") == True

def test_with_numbers():
    assert Solution().isPalindrome("0P") == False

if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_empty_after_filter()
    test_all_special_chars()
    test_single_char()
    test_with_numbers()
    print("All tests passed.")
