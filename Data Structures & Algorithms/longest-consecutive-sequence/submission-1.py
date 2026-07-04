class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) to build — gives us O(1) membership checks
        nums_set = set(nums)
        longest = 0

        # O(n) — each number in the set is visited exactly once here
        for i in nums_set:
            current_seq = 0

            # Only start a walk if i is the beginning of a sequence.
            # If i-1 exists, some earlier iteration will (or already did)
            # cover i as part of its walk — so we skip it here.
            if (i - 1) not in nums_set:
                current_num = i + 1
                current_seq = 1

                # Walk forward along the sequence.
                # Each number visited here is a sequence member that will be
                # skipped by the outer loop (because its n-1 exists).
                # So across ALL iterations, this while loop runs at most n
                # times total — not n times per outer iteration.
                while current_num in nums_set:
                    current_seq += 1
                    current_num += 1

            longest = max(longest, current_seq)

        # Overall: O(n) build + O(n) outer loop + O(n) total while iterations
        # = O(n)
        return longest