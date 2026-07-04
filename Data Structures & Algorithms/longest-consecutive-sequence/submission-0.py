class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums_set:
            current_seq = 0
            if (i - 1) not in nums_set:
                current_num = i + 1
                current_seq = 1
                while current_num in nums_set:
                    current_seq += 1
                    current_num += 1
            longest = max(longest, current_seq)

        return longest
                
