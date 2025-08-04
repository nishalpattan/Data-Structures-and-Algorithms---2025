# Last updated: 8/3/2025, 9:02:19 PM
from threading import Condition
class BoundedBlockingQueue(object):
    """
    capacity -> max size of queue
    enqueue -> adds element to front of Queue
                if reaches capacity, calling thread is blocked
    dequeue -> return rear element of Queue and pop it
    size -> current number of elements in Queue
    """

    def __init__(self, capacity: int):
        self.c = Condition()
        self.capacity = capacity
        self.q = collections.deque()

    def enqueue(self, element: int) -> None:
        self.c.acquire()
        while self.size() == self.capacity:
            self.c.wait()
        self.q.append(element)
        self.c.notifyAll()
        self.c.release()
            
    def dequeue(self) -> int:
        self.c.acquire()
        while self.size() == 0:
            self.c.wait()
        res = self.q.popleft()
        self.c.notifyAll()
        self.c.release()
        return res
        

    def size(self) -> int:
        return len(self.q)