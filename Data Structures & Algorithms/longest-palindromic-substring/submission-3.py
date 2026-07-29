class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        res = ""
        for i in range(len(s)):
            palindrome1 = expand(i, i)  # for odd length
            palindrome2 = expand(i, i + 1)   #for even length
            if len(palindrome1) > len(res):
                res = palindrome1
            if len(palindrome2) > len(res):
                res = palindrome2
        return res