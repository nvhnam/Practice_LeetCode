class ValidParentheses:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_tag = {")" : "(", "}" : "{", "]" : "[" }
        for c in s:
            if c in closing_tag: 
                if stack and stack[-1] == closing_tag[c]:
                    stack.pop()
                else: return False
            else:
                stack.append(c)
        return True if not stack else False