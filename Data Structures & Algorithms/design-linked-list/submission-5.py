class ListNode: #have a class that define the node attributes
    def __init__(self, val):
        self.val = val
        self.next = None
        #self.prev = None

class MyLinkedList:
    def __init__(self):
        self.left= ListNode(0)
        self.right= ListNode(0)
        self.left.next=  self.right
        #self.right.prev = self.left

    def get(self, index: int) -> int:
        current = self.left.next
        while current != self.right and index > 0:
            current = current.next
            index -=1
        if current != self.right and index == 0:
            return current.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        #new_node.prev = self.left
        new_node.next = self.left.next
        self.left.next = new_node
        
        #self.left.next.prev = new_node
        
        

    def addAtTail(self, val: int) -> None:
        
        current = self.left
        while current.next != self.right:
            current = current.next
    

        new_node = ListNode(val)
        new_node.next = self.right
        current.next = new_node
        

        
        #new_node.prev = self.right.prev
        #self.right.prev.next = new_node
        #self.right.prev = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left
        while current.next != self.right and index > 0:
            current = current.next
            index -=1 # when I exit the loop it means that I am currently at that index that I need to insert on
        if index == 0:
            new_node = ListNode(val)
            new_node.next = current.next
            current.next = new_node
            
            # new_node.prev = current.prev
            # new_node.next = current
            # current.prev.next = new_node
            # current.prev = new_node
            

    def deleteAtIndex(self, index: int) -> None:
        current= self.left
        while current.next != self.right and index >0:
            current = current.next
            index -= 1
        if current.next != self.right and index == 0:
            #current.prev.next = current.next
            current.next = current.next.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)