from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_queue = deque()

        for i in range(0, len(nums)):
            if max_queue and max_queue[0] < (i -k + 1):
                max_queue.popleft()

            while max_queue and nums[max_queue[-1]] <= nums[i]:
                max_queue.pop()
            
            max_queue.append(i)

            if i >= k - 1:
                #append window max to res
                res.append(nums[max_queue[0]])

        return res