class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''time: O(N), space:O(N)'''

        if len(asteroids) < 2: return asteroids

        stack = []
        i, n = 0, len(asteroids)

        while (i < n):
            b = asteroids[i]
            if not stack:
                stack.append(b)
                i += 1
            else:
                a = stack[-1]
                if a > 0 and b < 0:
                    if abs(a) > abs(b):
                        i += 1
                    elif abs(a) == abs(b):
                        stack.pop()
                        i += 1
                    else:
                        stack.pop()
                else:
                    stack.append(b)
                    i += 1
        return stack
