"""


Assume that the child holding
the potato will be at the front of the queue. Upon passing the potato, the simulation will simply
dequeue and then immediately enqueue that child, putting her at the end of the line. She will
then wait until all the others have been at the front before it will be her turn again. After num
dequeue/enqueue operations, the child at the front will be removed permanently and another
cycle will begin. This process will continue until only one name remains (the size of the queue
is 1).

"""


from Queue import Queue

def hot_potato(name_list, num):
    
    name_queue = Queue()
    
    for name in name_list:
        name_queue.enqueue(name)
        
    while name_queue.size() > 1:
        
        for i in range(num):
            name_queue.enqueue(name_queue.dequeue())
            
        name_queue.dequeue()
        
    return name_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent",
"Brad"], 7))