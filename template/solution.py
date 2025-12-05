from common.base import TextBaseSolution
import numpy as np
import os

class Solution1(TextBaseSolution):
    def solve(self) -> tuple[str, str]:
        raise NotImplementedError

class Solution2(TextBaseSolution):
    def solve(self) -> tuple[str, str]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution1(f"{os.path.dirname(__file__)}/example.txt")
    out = s.solve()
    print(out)  