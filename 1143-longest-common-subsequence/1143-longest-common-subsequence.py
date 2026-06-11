class Solution:
    def longestCommonSubsequence(self, x: str, y: str) -> int:
        dp = {}
        def lcs(x: str, y: str, n:  int, m: int) -> int:
            if n == 0 or m == 0 :
                return 0

            if (n, m) in dp:
                return dp[(n,m)]

            if x[n-1] == y[m-1] :
                dp[(n,m)] = 1 + lcs(x, y, n-1, m-1)
            else:
                dp[(n,m)] = max(lcs(x, y, n-1, m), lcs(x, y, n, m-1))
            return dp[(n,m)]
        return lcs(x, y, len(x), len(y))