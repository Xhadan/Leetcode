class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            # Check if the token is an operator
            if t in "+-*/":
                # The first pop is the 'right' side (b), 
                # the second pop is the 'left' side (a)
                b, a = stack.pop(), stack.pop()
                
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    # Special division logic for truncating toward zero
                    division = a / b
                    if division < 0:
                        stack.append(math.ceil(division))
                    else:
                        stack.append(math.floor(division))
            else:
                # If it's a number, convert to int and push to stack
                stack.append(int(t))
        
        # The result is the last remaining item on the stack
        return stack[0]