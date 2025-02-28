
"""

1. Create an empty stack called op_stack for keeping operators. Create an empty list for
output.
2. Convert the input infix string to a list by using the string method split.
3. Scan the token list from left to right.
• If the token is an operand, append it to the end of the output list.
• If the token is a left parenthesis, push it on the op_stack.
• If the token is a right parenthesis, pop the op_stack until the corresponding left
parenthesis is removed. Append each operator to the end of the output list.
• If the token is an operator, *, /, +, or −, push it on the op_stack. However, first
remove any operators already on the op_stack that have higher or equal precedence
and append them to the output list.

"""


from Stack import Stack

infix_expr = "( A + B ) * C"

#Create result list
result = []

#Create op_stack for keeping operators
op_stack = Stack()

#Convert infx expression to list with split method
infix_expr_list = infix_expr.split()

#Create a dict to hold the precedence levels of the operators
prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}


for token in infix_expr_list:
   
    if token == "(":
        op_stack.push(token)
        
    elif token.isalnum():
        result.append(token)
    
    elif token == ")":
        top_token = op_stack.pop()
        
        while top_token != "(":
            result.append(top_token)
            top_token = op_stack.pop()
            
    else:
        while  (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
             result.append(op_stack.pop())
        
        op_stack.push(token)
             
while not op_stack.is_empty():
    result.append(op_stack.pop())
    
print("".join(result))

