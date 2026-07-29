# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
           prev.next = None
        
        left = None
        right = slow

        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp

        dummy = ListNode(-1)
        tail = dummy

        original_head = head
        while head and left:
            tail.next = head
            tail = tail.next
            head = head.next

            tail.next = left
            tail = tail.next
            left = left.next
        tail.next = head if head else left

        original_head.val = dummy.next.val
        original_head.next = dummy.next.next
