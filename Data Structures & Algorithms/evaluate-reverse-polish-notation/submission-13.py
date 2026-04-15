class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        so what it is asking is to do is to use Reverse Polish Notation, it will give me a 
        array of intergers and operators that i need to find the totallity of 

        potential solution: iterate through the array, adding to a stack, once we hit an 
        operator we can pop the 2 previous operands from the stack and perform the operation
        """

        stack = []

        for index, token in enumerate(tokens):
            print(stack)
            if token == "+":
                temp = stack.pop()
                stack.append(stack.pop() + temp)
            elif token == "-":
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif token == "*":
                temp = stack.pop()
                stack.append(stack.pop() * temp)
            elif token == "/":
                temp = stack.pop()
                stack.append(int(stack.pop() / temp))
            else:
                token = int(token)
                # if 0 > token:
                #     token *= -1
                stack.append(token)
        
        print(stack)
        return stack[0]
