# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#assign the value on the right to the property on the left.

# previous_pointer         current_pointer
#       ↓                        ↓
#     None                      [1] -> [2] -> [3] -> None

# previous_pointer     current_pointer
#                                ↓                    ↓
#     None <- [1]               [1]                  [2] -> [3] -> None

# previous_pointer    current_pointer
#                                                     ↓                   ↓
#     None <- [1] <- [2]                             [2]                 [3] -> None

# previous_pointer     current_pointer
#                                                                        ↓                    ↓
#     None <- [1] <- [2] <- [3]                                         [3]                  None
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        current_pointer = head
        previous_pointer = None
        while (current_pointer != None):
            next_node = current_pointer.next # to save node 2 so that we don't lose it
            current_pointer.next = previous_pointer
            #(We break Node [1]'s forward arrow and point it backward to None. It is now the end of our new list!)
            previous_pointer = current_pointer
            current_pointer = next_node # not the current pointer is pointing to the node [2]
            
        return previous_pointer



        