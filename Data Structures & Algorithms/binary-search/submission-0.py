class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m  # Fixed: removed brackets
            elif nums[m] < target:
                l = m + 1
            else:  # Fixed: just else with colon
                r = m - 1 
        return -1