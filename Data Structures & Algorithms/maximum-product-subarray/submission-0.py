class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            tempmax = max(curr, max_prod * curr, min_prod * curr)
            min_prod = min(curr, max_prod * curr, min_prod * curr)
            max_prod = tempmax
            result = max(result, max_prod)
        return result