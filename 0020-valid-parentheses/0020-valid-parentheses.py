class Solution:
    def isValid(self, s: str) -> bool:
        brac = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for i in s:
            if i in brac.values():
                stack.append(i)
            elif stack and stack[-1] == brac[i]:
                stack.pop()
            else:
                return False
        return stack == []