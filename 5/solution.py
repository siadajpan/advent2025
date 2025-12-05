from common.base import TextBaseSolution
import numpy as np
from pathlib import Path
def read_file(data):
    ranges = []
    values = []
    ranges_on = True
    for line in data:
        if line == "":
            ranges_on = False
            continue
        if ranges_on:
            ranges.append(np.array(line.split("-"), dtype=int))
        else:
            values.append(int(line))
    ranges = np.array(ranges)
    values = np.array(values)
    print(ranges)
    print(values)
    return ranges, values

class Solution1(TextBaseSolution):

    def solve(self):
        ranges, values = read_file(self.data)
        fresh_amount = 0
        for v in values:
            if np.any((ranges[:, 0] <= v) & (ranges[:, 1] >= v)):
                fresh_amount += 1
        return fresh_amount

class Solution2(TextBaseSolution):
    def solve(self) -> tuple[str, str]:
        ranges, _ = read_file(self.data)
        ranges = ranges.tolist()
        stop = False
        while not stop:
            stop = True
            for i, r in enumerate(ranges):
                for j, r_rest in enumerate(ranges):
                    if i == j:
                        continue
                    # print("checking ranges", r, r_rest)
                    if (r_rest[0] >= r[0]) & (r_rest[0] <= r[1]) \
                    or (r_rest[1] >= r[0]) & (r_rest[1] <= r[1]):
                        print("found extension", r, r_rest)
                        print("new range", [min(r[0], r_rest[0]), max(r[1], r_rest[1])])
                        ranges.append([min(r[0], r_rest[0]), max(r[1], r_rest[1])])
                        ranges.pop(max(i,j))
                        ranges.pop(min(i,j))
                        stop = False
                        break
            print("now ranges", ranges)
        out = sum([r[1] - r[0] + 1 for r in ranges])
        return out

if __name__ == "__main__":
    path = Path(__file__).parent 
    # s = Solution1(path / "example.txt")
    # s = Solution1(path / "input.txt")
    # s = Solution2(path / "example2.txt")
    s = Solution2(path / "input.txt")
    out = s.solve()
    # 362700599443304
    print(out)  