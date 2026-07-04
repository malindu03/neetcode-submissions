class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer O(1) space
        n = len(height)
        if n == 0:
            return 0

        l, r = 1, n - 2
        max_left, max_right = height[0], height[n-1]
        total = 0

        while l <= r:
            if max_left <= max_right:
                water = max_left - height[l]
                max_left = max(max_left, height[l])
                if water > 0 :
                    total += water
                l += 1
            else:
                water = max_right - height[r]
                max_right = max(max_right, height[r])
                if water > 0:
                    total += water
                r -= 1

        return total