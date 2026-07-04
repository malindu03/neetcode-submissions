class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for x in nums:
            res[x] = res.get(x, 0) + 1

        for key, value in res.items():
            buckets[value].append(key)

        top_k = []
        for item in reversed(buckets):
            if item:
                top_k.extend(item)
            
            if len(top_k) >= k:
                break

        return top_k[:k]

            

        

        