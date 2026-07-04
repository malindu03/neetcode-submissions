class Solution:
    def trap(self, height: List[int]) -> int:
        wall_to_left = [0 for i in range(len(height))]
        wall_to_right = [0 for i in range(len(height))]

        for i in range(1,len(height)):
            wall_to_left[i] = max(wall_to_left[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):
            wall_to_right[i] = max(wall_to_right[i+1], height[i+1])

        total = 0
        for i in range(len(height)):
            water = min(wall_to_left[i], wall_to_right[i]) - height[i]
            if water > 0:
                total += water

        return total

