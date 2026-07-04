class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        bracket_map = {"(":")", "{":"}", "[":"]"}
        stack = []

        for x in s:
            if x in bracket_map:
                stack.append(x)
                continue
            if not stack:
                return False
            current = stack.pop()
            if bracket_map[current] != x:
                return False


        return len(stack) == 0
