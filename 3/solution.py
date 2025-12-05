from common.base import TextBaseSolution
import numpy as np

class Solution1(TextBaseSolution):
    def solve(self) -> tuple[str, str]:
        sum_jolts = 0
        for bank in self.data:
            # print(bank)
            numbers = [int(a) for a in bank]
            tens = np.max(numbers[:-1])
            tens_index = np.argmax(numbers[:-1])
            ones = np.max(numbers[tens_index + 1:])
            jolts = tens * 10 + ones
            # print(jolts)
            sum_jolts += jolts

        return str(sum_jolts), ""

class Solution2(TextBaseSolution):
    def solve(self) -> tuple[str, str]:
        sum_jolts = 0
        for bank in self.data:
            jolts = 0
            curr_index = 0
            numbers = [int(a) for a in bank]
            for d in range(11, 0, -1):
                print(numbers, d, numbers[curr_index:-d])
                jolts += np.max(numbers[curr_index:-d]) * 10 ** d
                curr_index += np.argmax(numbers[curr_index:-d]) + 1
                print(jolts, curr_index)
            d=0
            print(bank, d, numbers[curr_index:])
            jolts += np.max(numbers[curr_index:]) 
            print(jolts)
            sum_jolts += jolts
        return str(sum_jolts), ""


if __name__ == "__main__":
    print(Solution1("3/example.txt").solve())
    print(Solution1("3/input.txt").solve())
    print(Solution2("3/example.txt").solve())
    print(Solution2("3/input.txt").solve())