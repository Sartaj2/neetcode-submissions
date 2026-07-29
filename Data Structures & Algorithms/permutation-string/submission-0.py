class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashmap1 = {}
        for ch in s1:
            hashmap1[ch] = hashmap1.get(ch, 0) + 1

        hashmap2 = {}
        left = 0
        for right in range(len(s2)):
            hashmap2[s2[right]] = hashmap2.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                hashmap2[s2[left]] -= 1
                if hashmap2[s2[left]] == 0:
                    del hashmap2[s2[left]]
                left += 1

            if hashmap2 == hashmap1:
                return True

        return False