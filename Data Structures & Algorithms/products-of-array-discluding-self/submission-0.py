class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_nums = [1 for _ in range(len(nums))]
        suffix_nums = [1 for _ in range(len(nums))]

        # make prefix list
        for i in range(len(nums)):
            if i == 0:
                continue
            prefix_nums[i] = prefix_nums[i-1] * nums[i-1]

        # make suffix list  
        for i in range(len(nums)-1, -1, -1):
            if i == (len(nums) - 1):
                continue

            suffix_nums[i] = suffix_nums[i+1] * nums[i+1]

        res = []
        for i in range(len(nums)):
            res.append(prefix_nums[i] * suffix_nums[i])

        return res