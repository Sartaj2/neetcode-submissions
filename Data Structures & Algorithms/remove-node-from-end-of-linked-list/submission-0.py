# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n + 1):
            if fast is not None:
               fast = fast.next
            else:
               break


        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
