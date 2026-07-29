# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        carry = 0

        while l1 != None or l2 != None or carry != 0:
              x = l1.val if l1 is not None else 0
              y = l2.val if l2 is not None else 0
              total = x + y + carry
              carry = total // 10
              modulo = ListNode(total%10)
              current.next = modulo
              current = current.next
              l1 = l1.next if l1 else None
              l2 = l2.next if l2 else None

        return dummy.next