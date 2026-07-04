class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        candidate = (max(piles) + 1, max(piles) + 1)

        hi = max(piles)
        lo = 1
        # we go over the possible answers not the given array
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            total_hours = sum(math.ceil(x/mid) for x in piles)

            if total_hours > h:
                lo = mid + 1
            else :
                candidate = (mid, total_hours)
                hi = mid - 1

        return candidate[0]