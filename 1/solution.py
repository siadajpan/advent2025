from common.base import TextBaseSolution

class Solution1(TextBaseSolution):
    def solve(self) -> tuple[str, str]:
        zeros = 0
        data = self.data
        curr_number = 50
        for rotation in data:
            direction, steps = rotation[0], int(rotation[1:])
            sign = 1 if direction == "R" else -1
            curr_number += steps * sign
            curr_number = curr_number % 100
            zeros += 1 if curr_number == 0 else 0
        return zeros

class Solution2(TextBaseSolution):
    def solve(self) -> tuple[str, str]:
        zeros = 0
        data = self.data
        curr_number = 50
        for rotation in data:
            direction, steps = rotation[0], int(rotation[1:])
            zeros_add = -1 if curr_number == 0 and direction == "L" else 0
            sign = 1 if direction == "R" else -1
            curr_number += steps * sign
            zeros_add += 1 if curr_number == 0 else 0
            zeros_add += 1 if curr_number % 100 == 0 and curr_number < 0 else 0
            zeros_add += abs(curr_number // 100)
            curr_number = curr_number % 100
            zeros += zeros_add
        return zeros


s = Solution2("1/example.txt")
zeros = s.solve()
print(zeros)
s = Solution2("1/input.txt")
zeros = s.solve()
print(zeros)

