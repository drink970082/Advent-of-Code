def part1(input):
    m, n = len(input), len(input[0])
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    res = 0
    for i in range(m):
        for j in range(n):
            cnt = 0
            if input[i][j] == "@":
                for d in dir:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n:
                        if input[ni][nj] == "@":
                            cnt += 1
                if cnt < 4:
                    res += 1
    return res


def part2(input):
    m, n = len(input), len(input[0])
    input = [list(row) for row in input]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    res = 0
    while True:
        to_remove = []
        for i in range(m):
            for j in range(n):
                cnt = 0
                if input[i][j] == "@":
                    for d in dir:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < m and 0 <= nj < n:
                            if input[ni][nj] == "@":
                                cnt += 1
                    if cnt < 4:
                        to_remove.append((i, j))
        if not to_remove:
            break
        for i, j in to_remove:
            input[i][j] = "."
            res += 1
    return res