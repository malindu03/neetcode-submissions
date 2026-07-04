class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        increasing_stack = []

        for i, temp in enumerate(temperatures):
            
            while increasing_stack and temperatures[increasing_stack[-1]] < temp:
                index = increasing_stack.pop()
                res[index] = i - index
            increasing_stack.append(i)
        return res
            