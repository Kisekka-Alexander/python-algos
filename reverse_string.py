str = "alexander"

def reverse_str(str):
    if len(str) == 1:
        return str[0]
    
    else:
        # result += reverse_str(str[1:])
        return reverse_str(str[1:]) + str[0]
print(reverse_str("alexander")) 