class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def backtracking(i, subset):
            if i == len(s):
                res.append(temp.copy())
                return
            for j in range (i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    temp.append(s[i:j+1])
                    backtracking(j+1, temp)
                    temp.pop()
        backtracking (0, temp)
        return res