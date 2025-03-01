class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.insert(0,item)
        
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.queue == []
    
    def dequeue(self):
        return self.queue.pop()