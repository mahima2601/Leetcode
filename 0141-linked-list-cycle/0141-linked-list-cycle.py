# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow=head
        fast=head
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
            if fast.next!=None:
                fast=fast.next
            else:
                return False
            if slow==fast:
                return True
        return False

        

        