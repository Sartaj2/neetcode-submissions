class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set(wordDict)
        hashmap = {}
        def canSegment(start):
            if start == len(s):
                return True
            if start in hashmap:
                return hashmap[start]

            end = start + 1
            while end <= len(s):
                if s[start:end] in visited:
                    if canSegment(end):
                        hashmap[start] = True
                        return True
                end += 1
            hashmap[start] = False
            return False
        return canSegment(0)
