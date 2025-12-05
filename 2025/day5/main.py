def part1(input):
    ranges = []
    nums = []
    for i in input:
        if i == "":
            continue
        if "-" in i:
            ranges.append([int(n) for n in i.split("-")])
        else:
            nums.append(int(i))
    ranges.sort(key=lambda x: x[0])
    intervals = [ranges[0]]
    for r in ranges:
        if intervals[-1][1] >= r[0]:
            intervals[-1][1] = max(intervals[-1][1], r[1])
        else:
            intervals.append(r)
    res = 0
    for n in nums:
        left = 0
        right = len(intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] <= n <= intervals[mid][1]:
                res += 1
                break
            elif intervals[mid][0] > n:
                right = mid - 1
            else:
                left = mid + 1
    return res


def part2(input):
    ranges = []
    for i in input:
        if "-" in i:
            ranges.append([int(n) for n in i.split("-")])
    ranges.sort(key=lambda x: x[0])
    intervals = [ranges[0]]
    for r in ranges:
        if intervals[-1][1] >= r[0]:
            intervals[-1][1] = max(intervals[-1][1], r[1])
        else:
            intervals.append(r)
    return sum([r[1] - r[0] + 1 for r in intervals])
