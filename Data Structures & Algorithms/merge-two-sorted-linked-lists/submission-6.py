# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1 and list2 is None:
            return list1 or list2
        dummy_head = ListNode() # to make up a fake head 
        current = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next
                
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

    

        return dummy_head.next


        