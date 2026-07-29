class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def backtracking(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            #All subsets that incluse nums[i]
            subset.append(nums[i])
            backtracking (i + 1, subset)

            subset.pop()
            # All subset that dont include nums[i]
            while i + 1 < len(nums) and nums[i] == nums [i + 1]:
             i += 1

            backtracking (i + 1, subset)
        backtracking(0, [])
        return res
