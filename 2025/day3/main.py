def part1(input):
    res = 0
    for i in input:
        for st in range(9, -1, -1):
            if str(st) in i:
                idx = i.index(str(st))
                if idx + 1 < len(i):
                    end = max([int(x) for x in i[idx + 1 :]])
                else:
                    continue
                res += st * 10 + end
                break
    return res


def part2(input):
    def search(s, remaining):
        if remaining == 0:
            return ""
        for i in range(9, -1, -1):
            if str(i) in s:
                idx = s.index(str(i))
                if idx < len(s) - remaining:
                    return str(i) + search(s[idx + 1 :], remaining - 1)
                elif idx == len(s) - remaining:
                    return s[idx : idx + remaining]
                else:
                    continue
        return ""

    res = 0
    for i in input:
        s = search(i, 12)
        if s:
            res += int(s)
    return res
