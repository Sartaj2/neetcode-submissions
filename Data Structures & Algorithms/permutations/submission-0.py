class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False
        
        used = [False] * len(nums)
        backtrack([], used)
        return res