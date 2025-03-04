class Node:
    
    def __init__(self,data):
        self.item = data
        self.next = None
    
    def set_data(self, new_data):
        self.item = new_data
        
    def get_data(self):
        return self.item
    
    def get_next(self):
        return self.next 
    
    def set_next(self, new_next):
        self.next = new_next
        
        
class UnorderedList:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
            
        return count
    
    def search(self, item):
        current = self.head
        found = False
        
        while current and not found:
            if(current.get_data() == item):
                found = True
            else:
                current = current.get_next()
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if(current.get_data() == item):
                found = True
                
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
            
        else:
            previous.set_next(current.get_next)
            
    def pop(self):
        pass
    
    def append(self, item):
        pass
    
    def insert(self, ind, item):
        pass
    
    def index(self, item):
        pass

        
    
    