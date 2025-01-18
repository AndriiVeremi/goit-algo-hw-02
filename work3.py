def symmetrically(expression):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = []

    for char in expression:
        if char in brackets:
            stack.append(char)   
        elif char in brackets.values():   
            if stack and brackets[stack[-1]] == char:
                stack.pop()  
            else:
                return f"{expression} Несиметрично"

    return f"{expression} Симетрично" if not stack else f"{expression} Несиметрично"



print(symmetrically("( ){[ 1 ]( 1 + 3 )( ){ }}")) 
print(symmetrically("( 23 ( 2 - 3);"))            
print(symmetrically("( 11 }"))



