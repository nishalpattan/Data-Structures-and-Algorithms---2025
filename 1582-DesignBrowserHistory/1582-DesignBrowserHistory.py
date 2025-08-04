# Last updated: 8/3/2025, 9:01:57 PM
class DNode:
    def __init__(self,val, prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_page = DNode(homepage)

    def visit(self, url: str) -> None:
        visit_page = DNode(url)
        self.curr_page.next = visit_page
        visit_page.prev = self.curr_page
        self.curr_page = self.curr_page.next
        
    def back(self, steps: int) -> str:
        while steps > 0 and self.curr_page.prev:
            self.curr_page = self.curr_page.prev
            steps -= 1
        return self.curr_page.val
    
    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr_page.next:
            self.curr_page = self.curr_page.next
            steps -= 1
        return self.curr_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)