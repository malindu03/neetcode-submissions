class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            try:
                num = int(x)
                stack.append(num)
            except ValueError:
                int1 = stack.pop()
                int2 = stack.pop()
                res = 0
                if x == "+":
                    res = int2 + int1
                elif x == "-":
                    res = int2 - int1
                elif x == "*":
                    res = int2 * int1
                else:
                    res = int(int2 / int1)
            
                stack.append(res)

        return stack.pop()


