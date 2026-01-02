def part1(input):
    res = 0
    block = {}
    for i in range(6):
        _, fr, sr, tr, _ = input[5 * i : 5 * i + 5]
        block[i] = fr.count("#") + sr.count("#") + tr.count("#")
    for i in range(30, len(input)):
        a, puzzle = input[i].split(":")
        area = int(a[0:2]) * int(a[3:5])
        puzzles = [int(p) for p in puzzle.split(" ") if p]
        curr_area = 0
        for i in range(6):
            curr_area += puzzles[i] * block[i]
        if area >= curr_area:
            res += 1
    return res


def part2(input):
    return
