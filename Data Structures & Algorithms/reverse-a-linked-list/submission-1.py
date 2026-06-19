# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return head
            array_to_store = []
            while head:
                array_to_store.append(head.val)
                head = head.next
    
            array_to_store.reverse()
            dummy_head = ListNode(array_to_store[0])
            current = dummy_head

            print()
            for value in array_to_store[1:]:
                current.next = ListNode(value)
                current = current.next
            return dummy_head 
        