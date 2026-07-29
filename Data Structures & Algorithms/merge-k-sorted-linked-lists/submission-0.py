# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dummy node is a great way to start, it simplifies edge cases.
        dummy = ListNode(-1)
        # 'res' will be our pointer that builds the new list.
        res = dummy
        k = len(lists)

        # This outer loop will run until all lists are empty.
        while True:
            # --- CORRECTION ---
            # We must find the minimum node in each iteration.
            # We'll track the index of the list with the smallest current value.
            min_index = -1
            min_val = float('inf')

            # --- CORRECTION ---
            # This inner loop's purpose is to find the node with the minimum
            # value among the heads of all the lists.
            for i in range(k):
                # We only consider lists that are not empty.
                if lists[i] is not None:
                    # If this list's head value is smaller than the minimum we've seen so far...
                    if lists[i].val < min_val:
                        # ...we update our minimum value and store the index of this list.
                        min_val = lists[i].val
                        min_index = i
            
            # --- CORRECTION ---
            # If, after checking all lists, min_index is still -1, it means
            # all the lists were empty. We can break out of the main loop.
            if min_index == -1:
                break

            # --- CORRECTION ---
            # Append the node from the list we identified (at min_index) to our result.
            res.next = lists[min_index]
            # Move our result pointer forward.
            res = res.next
            # Advance the pointer of the list we just took the node from.
            lists[min_index] = lists[min_index].next
            
        # The final merged list starts right after our dummy node.
        return dummy.next
