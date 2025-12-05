from common.base import TextBaseSolution
import numpy as np

class Solution1(TextBaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = np.array([[el for el in x] for x in self.data])

    def get_neighbours(self, x, y):
        return self._data[max(0, x-1):min(x+2, self._data.shape[0]), max(0, y-1):min(y+2, self._data.shape[1])] 

    def solve(self) -> tuple[str, str]:
        accessible = 0
        for row in range(self._data.shape[0]):
            for col in range(self._data.shape[1]):
                if self._data[row][col] == ".":
                    continue
                all_neighbours = "".join(self.get_neighbours(row, col).flatten())
                papers = all_neighbours.count("@")
                if papers < 5:
                    accessible += 1
                    self._data[row][col] = "."
        return accessible
        
class Solution2(TextBaseSolution):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.solver = Solution1(file_path)

    def solve(self) -> tuple[str, str]:
        more_to_access = True   
        total_accessible = 0
        while more_to_access:
            accessible = self.solver.solve()
            total_accessible += accessible
            if accessible == 0:
                break
        return total_accessible
    

if __name__ == "__main__":
    # s = Solution1("4/example.txt")
    # out = s.solve()
    # s = Solution1("4/input.txt")
    # out = s.solve()
    # s = Solution2("4/example.txt")
    # out = s.solve()
    s = Solution2("4/input.txt")
    out = s.solve()

    print(out)  