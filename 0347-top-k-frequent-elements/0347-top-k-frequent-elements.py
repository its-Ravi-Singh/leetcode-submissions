class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for i in nums:
            count_dict[i] += 1
        return list(map(lambda item: item[0] ,sorted(count_dict.items(), key = lambda item: item[1], reverse=True)[:k]))
