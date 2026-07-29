class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, target):
            if target == 0:
               res.append(subset.copy())
               return
            if target < 0 or i >= len(nums):
               return

            subset.append(nums[i])
            dfs(i, subset, target - nums[i])
            subset.pop()
            dfs(i + 1, subset, target)
        dfs(0, [], target)
        return res