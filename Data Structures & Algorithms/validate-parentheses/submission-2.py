class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            print(stack)
            print(c)

            match c:
                case "(":
                    print(stack)
                    stack.append("(")
                case ")":
                    print(stack)
                    if not stack: return False
                    if stack[-1] != "(": return False
                    stack.pop()
                case "{":
                    print(stack)
                    stack.append("{")
                case "}":
                    print(stack)
                    if not stack: return False
                    if stack[-1] != "{": return False
                    stack.pop()
                case "[":
                    print(stack)
                    stack.append("[")
                case "]":
                    print(stack)
                    if not stack: return False
                    if stack[-1] != "[": return False
                    stack.pop()
            
        if not stack:
            return True
            
        return False