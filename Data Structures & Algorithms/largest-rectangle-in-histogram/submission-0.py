class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        inc_stack = []

        for i in range(len(heights)):
            # i is the index
            while inc_stack and (heights[inc_stack[-1]] > heights[i]):
                temp = inc_stack.pop()

                if inc_stack:
                    temp_area = heights[temp] * (i - inc_stack[-1] - 1)
                else:
                    temp_area = heights[temp] * i

                max_area = max(max_area, temp_area)

            inc_stack.append(i)

        # if stack remains
        while inc_stack:
            temp = inc_stack.pop()
            i = len(heights)
            if inc_stack:
                temp_area = heights[temp] * (i - inc_stack[-1] - 1)
            else:
                temp_area = heights[temp] * i
            max_area = max(max_area, temp_area)

        return max_area
