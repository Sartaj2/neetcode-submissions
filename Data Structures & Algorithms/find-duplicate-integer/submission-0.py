from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the intersection point in the cycle.
        # Initialize pointers based on the array values.
        slow = nums[0]
        fast = nums[0]

        while True:
            # Move slow one step.
            slow = nums[slow]
            # Move fast two steps.
            fast = nums[nums[fast]]
            
            # If they meet, break the loop to start Phase 2.
            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle (the duplicate).
        # Reset one pointer to the start of the "list".
        slow2 = nums[0] 
        
        # Move both pointers one step at a time until they meet.
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        # The meeting point is the duplicate number.
        return slow