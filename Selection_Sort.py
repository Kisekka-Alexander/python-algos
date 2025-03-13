def selection_sort(a_list):
    pass_nums = len(a_list) - 1
    
    while pass_nums > 0:
        pos_of_max = 0
        for i in range(1,pass_nums+1):
            if a_list[i] > a_list[pos_of_max]:
                pos_of_max = i
                
        a_list[pass_nums] , a_list[pos_of_max] = a_list[pos_of_max], a_list[pass_nums]
        pass_nums -= 1
        
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)