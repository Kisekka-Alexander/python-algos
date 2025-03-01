from Stack import Stack

def postfix_evaluation():
    operand_stack = Stack()

    expression = "7 8 + 3 2 + /"

    expression_to_list = expression.split()

    for token in expression_to_list:
        if token in "0123456789":
            operand_stack.push(int(token))
            
        else:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            result = do_math(token, op1, op2)
            operand_stack.push(result)
            
    return operand_stack.pop()

def do_math(operator, op1, op2) -> int:
    if operator == "/":
        return op1 / op2
    elif operator == "*":
        return op1 * op2
    elif operator == "+":
        return op1 + op2
    else:
        return op1 - op2
    
print(postfix_evaluation())