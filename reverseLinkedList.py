# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        current, previous = head, None
        while left > 1:
            previous = current
            current = current.next
            left -= 1
            right -= 1

        tail, connection = current, previous
        while right:
            third = current.next
            current.next = previous
            previous = current
            current = third
            right -= 1

        if connection:
            connection.next = previous
        else:
            head = previous
        tail.next = current
        return head
        