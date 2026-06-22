class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)
        print(d)
        return min(d["b"], d["a"], d["l"] >> 1, d["o"] >> 1, d["n"])