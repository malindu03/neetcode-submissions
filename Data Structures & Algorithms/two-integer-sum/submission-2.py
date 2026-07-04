class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for id, x in enumerate(nums):
            difference = target - x
            if difference in temp:
                return [int(temp[difference]), int(id)]
            temp[x] = id