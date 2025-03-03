class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def set_data(self, new_data):
        self.data = new_data
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next 
    
    def set_next(self, new_next):
        self.next = new_next
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        
        
    
    