class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = list(range(n + 1))
        def find(i: int) -> int:
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]
        for x, y, d in roads:
            root[find(x)] = find(y)
        res = 10**9
        g1 = find(1)
        for x, y, d in roads:
            if find(x) == g1:
                res = min(res, d)
        return res