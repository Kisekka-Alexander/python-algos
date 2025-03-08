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
            
            else: #If the slot is already occupied, rehash to find another slot
                
                next_slot = self.rehash_function(hash_value, len(self.slots))
                
                # Loop through the slots until you find an empty slot self.slots[next_slot] == None OR
                # Until you find a slot with the value == key 
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash_function(next_slot, len(self.slots))
                
                # If you find an empty slot then fill it   
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = val
                    
                # Otherwise if the next slot you find has value == key, then replace the value in the data table
                else:
                    self.data[next_slot] = val
                    
    
    def hash_function(self,key,size):
        return key % size
    
    def rehash_function(self,old_hash,size):
        return (old_hash + 1) % size