def part1(input):
    n, m = len(input), len(input[0])
    has_flow = [False] * m
    for j in range(m):
        if input[0][j] == "S":
            has_flow[j] = True
    split = 0
    for i in range(1, n):
        for j in range(m):
            if has_flow[j] and input[i][j] == "^":
                has_flow[j] = False
                if j - 1 >= 0:
                    has_flow[j - 1] = True
                if j + 1 < m:
                    has_flow[j + 1] = True
                split += 1
    return split


def part2(input):
    n, m = len(input), len(input[0])
    cnt = [0] * m
    for j in range(m):
        if input[0][j] == "S":
            cnt[j] = 1

    for i in range(1, n):
        nxt_cnt = [0] * m
        for j in range(m):
            if cnt[j] and input[i][j] == "^":
                if j - 1 >= 0:
                    nxt_cnt[j - 1] += cnt[j]
                if j + 1 < m:
                    nxt_cnt[j + 1] += cnt[j]
            else:
                nxt_cnt[j] += cnt[j]
        cnt = nxt_cnt
    return sum(cnt)
