# Last updated: 8/3/2025, 9:02:56 PM
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
        
        # Brute Force approach using stacks
        # self.stack = list()
        # self.hash_map = dict()
    
    def _hash(self,key):
        return key % self.keyRange
    
    def add(self, key: int) -> None:
        # Brute Force approach using stacks
        # if not self.contains(key):
        #     self.stack.append(key)
        #     self.hash_map[key] = True
        hash_of_key = self._hash(key)
        self.bucketArray[hash_of_key].insert(key)
        

    def remove(self, key: int) -> None:
        # Brute Force approach using stacks
        # if self.contains(key):
        #     self.stack.remove(key)
        #     self.hash_map[key] = False
        hash_of_key = self._hash(key)
        self.bucketArray[hash_of_key].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # Brute Force approach using stacks
        # return self.hash_map.get(key,False)

        # Using Linked List as bucket for collision resolution
        hash_of_key = self._hash(key)
        return self.bucketArray[hash_of_key].contains(key)
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def insert(self, key):
        if not self.contains(key):
            new_node = Node(key, self.head.next)
            self.head.next = new_node
    
    def remove(self, key):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
    
    def contains(self, key):
        curr_head = self.head.next
        while curr_head:
            if curr_head.val == key:
                return True
            curr_head = curr_head.next
        return False
        
    
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)