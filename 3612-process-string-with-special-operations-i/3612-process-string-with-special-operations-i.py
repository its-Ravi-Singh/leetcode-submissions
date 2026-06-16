class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for i in s:
            match i:
                case '#':
                    ans += ans
                case '%':
                    ans = ans[::-1]
                case '*':
                    ans = ans[:-1]
                case _:
                    ans += i
        return ans