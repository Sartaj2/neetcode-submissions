class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        hashmap = {}

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            window_size = right - left + 1
            max_freq = max(hashmap.values())

            if window_size - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
