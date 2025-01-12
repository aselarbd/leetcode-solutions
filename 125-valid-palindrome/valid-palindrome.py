class Solution:
    def isPalindrome(self, s: str) -> bool:

        process = [ch.lower() for ch in s if ch.isalnum()]

        return process == process[::-1]