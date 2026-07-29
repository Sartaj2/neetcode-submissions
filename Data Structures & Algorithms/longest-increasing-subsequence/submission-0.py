class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for curr in nums:
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < curr:
                    l = mid + 1
                else:
                    r = mid - 1
            if l == len(tails):
                tails.append(curr)
            else:
                tails[l] = curr
        return len(tails)