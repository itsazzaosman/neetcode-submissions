class ListNode:
    def __init__ (self, val, prev= None, next=None):
        self.val = val
        self.prev = prev
        self.next = next



class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode (homepage)
        

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.current
        self.current.next = node
        self.current =  node
        
    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -=1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)