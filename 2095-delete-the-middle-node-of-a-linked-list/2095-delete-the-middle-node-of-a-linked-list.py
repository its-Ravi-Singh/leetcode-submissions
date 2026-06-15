# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        container = deque()
        cur = head
        while cur:
            container.append(cur)
            cur = cur.next
        
        mid = len(container) // 2

        prev_node = container[mid - 1]
        node_to_rem = container[mid]

        prev_node.next = node_to_rem.next

        return head