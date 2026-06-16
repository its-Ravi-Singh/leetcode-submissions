class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for i in s:
            if i == "*":
                ans = ans[:-1]
            elif i == "#":
                ans = ans+ans
            elif i == "%":
                ans = ans[::-1]
            else:
                ans += i
        return ans