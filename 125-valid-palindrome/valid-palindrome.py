class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(ch for ch in s if ch.isalnum()).lower()

        return new_s == new_s[::-1]
        