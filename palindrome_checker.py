from Deque import Deque

def palindrome_checker(word):
    
    deque = Deque()
    
    for s in word:
        deque.add_rear(s)
        
    still_true = True
    
    while deque.size() > 1 and still_true:
        
        first = deque.remove_rear()
        last = deque.remove_front()
        
        if first != last:
            still_true = False
            
    return still_true

print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))