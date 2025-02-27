
"""

1. Create an empty stack called operand_stack.
2. Convert the string to a list by using the string method split.
3. Scan the token list from left to right.
• If the token is an operand, convert it from a string to an integer and push the value
onto the operand_stack.
• If the token is an operator, *, /, +, or −, it will need two operands. Pop the
operand_stack twice. The first pop is the second operand and the second pop is
the first operand. Perform the arithmetic operation. Push the result back on the
operand_stack

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

