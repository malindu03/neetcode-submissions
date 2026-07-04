class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        pos_speed.sort(reverse=True)
        stack = []

        for pos, speed in pos_speed:
            time = (target - pos)/speed
            if not stack:
                stack.append(time)
                continue
            
            if time > stack[-1]:
                stack.append(time)

        return len(stack)

