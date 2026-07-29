class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset, target):
            if target == 0:
                res.append(subset.copy())
                return
            if target < 0 or i >= len(nums):
                return

            subset.append(nums[i])
            dfs (i + 1, subset, target - nums[i])

            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs (i + 1, subset, target)
        dfs(0, [], target)
        return res