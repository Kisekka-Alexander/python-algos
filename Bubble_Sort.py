def bubble_sort(a_list):
    passes = 0
    pass_nums = len(a_list) - 1
    while pass_nums > 0:
        for i in range(pass_nums):
            passes += 1
            if(a_list[i] > a_list[i+1]):
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        pass_nums -= 1
    print(passes)
                
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(a_list)
# print(a_list)


"""
A bubble sort can be modified to stop early if it finds that the list has become sorted. 
This means that for lists that require just a few passes, a bubble sort may have an advantage 
in that it will recognize the sorted list and stop.
The code below shows this modification, which is often referred to as the short bubble.

"""

def short_bubble_sort(a_list):
    exchange = True
    pass_nums = len(a_list) - 1
    passes = 0
    
    while pass_nums > 0 and exchange:
        exchange = False
        for i in range(pass_nums):
            if(a_list[i] > a_list[i+1]):
                exchange = True
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                passes += 1                
        pass_nums -= 1
    
    print(passes)
        
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
short_bubble_sort(a_list)
print(a_list)


"""
We can see that bubble sort performs 36 passes while the short buble sort performs 20 passes.
"""