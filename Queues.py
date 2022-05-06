
from collection import deque


class Queue:
    def __init__(self):
        self.items= deque()
        
    def is_empty(slef):
        return not self.item
        # return len(self.item)==0
        
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)
    
    
if __name__ == "__main__":
    q = Queue()
    print(q)