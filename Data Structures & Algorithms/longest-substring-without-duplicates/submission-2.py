class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        res = 0
        left = 0

        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)
            
            hashmap[s[right]] = right
            res = max(res, right - left + 1)
        return res