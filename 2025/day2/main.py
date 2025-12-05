def part1(input):
    ranges = input[0].split(",")
    res = 0
    for r in ranges:
        lower, upper = r.split("-")
        for i in range(int(lower), int(upper) + 1):
            num = str(i)
            if num[: len(num) // 2] == num[len(num) // 2 :]:
                res += i
    return res


def part2(input):
    ranges = input[0].split(",")
    res = 0
    for r in ranges:
        lower, upper = r.split("-")
        for i in range(int(lower), int(upper) + 1):
            num = str(i)
            if num in (num + num)[1:-1]:
                res += i
    return res