class HashTable:
    def __init__(self):
        self.size = []
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key ,val):
        hash_value = self.hash_function(key, len(self.slots))
        
        # Check if theres a value in the slots list at the index of hash_value
        if(self.slots[hash_value] == None):
            self.slots[hash_value] = key
            self.data[hash_value] = val
            
        else:
            if(self.slots[hash_value] == key):
                self.data[hash_value] = val #Replace the value 
            
            else:
                next_slot = self.rehash_function(hash_value, len(self.slots))
                
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash_function(next_slot, len(self.slots))
    
    def hash_function(self,key,size):
        return key % size
    
    def rehash_function(self,old_hash,size):
        return (old_hash + 1) % size