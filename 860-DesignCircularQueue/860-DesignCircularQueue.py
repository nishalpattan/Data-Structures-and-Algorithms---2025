# Last updated: 8/3/2025, 9:02:53 PM
class DLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:
    # tail is connected to the head

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        dummy_node = DLNode(-1, None)
        self.head = dummy_node
        self.tail = dummy_node
        
    def enQueue(self, value: int) -> bool:
        # adding to the end or tail
        # if capacity is full: return false
        # else: add to tail and return true
        if self.isFull(): return False
        new_node = DLNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            prev_node = self.tail
            prev_node.next = new_node
            new_node.prev = prev_node
            self.tail = new_node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # take the element from the start (FIFO) or head
        # if head is not pointing to any element : return false
        # else: return true after removing elem from head
        if self.isEmpty(): return False
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            next_head = self.head.next
            self.head = next_head
        self.size -= 1
        return True

    def Front(self) -> int:
        # get first element head is pointing to
        if self.isEmpty(): return -1
        node = self.head
        return node.val

    def Rear(self) -> int:
        # get last element tail is pointing to
        if self.isEmpty() : return -1
        node = self.tail
        return node.val

    def isEmpty(self) -> bool:
        # if size is 0
        return self.size == 0

    def isFull(self) -> bool:
        # if size is 1
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()