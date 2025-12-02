from common.base import TextBaseSolution
import numpy as np

class Solution1(TextBaseSolution):
    def solve_range(self, start, stop):
        print("original", start, stop)
        if len(str(start)) % 2 != 0:
            start = 10 ** (len(str(start)) )
        if len(str(stop)) % 2 != 0:
            stop = 10 ** (len(str(stop)) - 1) - 1
        print("modified", start, stop)
        if start > stop:
            return 0
        
        digits_start = len(str(start))
        digits_stop = len(str(stop))
        total_sum = 0
        for digits in range(digits_start, digits_stop+ 1):
            divider = 10 ** (digits / 2) + 1
            print("divider", divider)
            first_number = np.ceil(start / divider)
            last_number = np.floor(stop / divider)
            print(first_number, last_number)
            if first_number > last_number:
                return 0
            sum = ((last_number + first_number) * (last_number - first_number + 1) / 2) * divider
            print("sum", sum, "\n")
            total_sum += sum

        return total_sum
    
    def solve(self) -> tuple[str, str]:
        print("data", self.data[0])
        ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in self.data]
        print(ranges)
        total_sum = 0
        for r in ranges:
            range_sum = self.solve_range(r[0], r[1])
            total_sum += range_sum
        return total_sum


class Solution2(Solution1):
    def solve_range(self, start, stop):
        digits_start = len(str(start))
        digits_stop = len(str(stop))
        all_numbers = []
        print("\n*** solving for", start, stop)


        for digits in range(digits_start, digits_stop+ 1):
            loc_start = start
            loc_stop = stop
            print("digits", digits)
            if len(str(start)) != digits:
                loc_start = 10 ** (digits - 1)
            if len(str(stop)) != digits:
                loc_stop = 10 ** digits - 1
            print("modified", loc_start, loc_stop)
            for divider_ones in range(2, digits + 1):
                if digits % divider_ones != 0:
                    print(f"divider {divider_ones} does not divide {digits}")
                    continue
                print("divider_ones", divider_ones)
                multiplier = int(digits / divider_ones)
                divider = np.sum([10 ** (d * multiplier) for d in range(divider_ones)])
                print("divider", divider)
                first_number = np.ceil(loc_start / divider)
                last_number = np.floor(loc_stop / divider)
                print(first_number, last_number)
                if first_number > last_number:
                    continue
                # sum = ((last_number + first_number) * (last_number - first_number + 1) / 2) * divider
                all_numbers.extend(np.arange(first_number, last_number + 1) * divider)

                print("numbers", all_numbers, "\n")
        s = np.sum(list(set(all_numbers)))
        print("sum", s, "\n")


        return s


if __name__ == "__main__":
    # s = Solution1("2/example.txt", split_by=",")
    # out = s.solve()
    # print(out)

    s = Solution2("2/example.txt", split_by=",")
    out = s.solve()
    print(out)

    s = Solution2("2/input.txt", split_by=",")
    out = s.solve()
    print(out)
