class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        seen = Counter(nums)
        result = []

        sorted_items = sorted(seen.items(), key=lambda pair: pair[1], reverse=True)
        return [key for key, freq in sorted_items[:k]]
                
        