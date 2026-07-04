class Solution:
    def trap(self, height: List[int]) -> int:
        #stack
        if not height:
            return 0
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(left, right) - bottom
                    w = i - stack[-1] - 1
                    res += h * w

            stack.append(i)

        return res