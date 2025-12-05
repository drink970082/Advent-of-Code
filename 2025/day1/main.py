def part1(input):
    pos = 50
    cnt = 0
    for i in input:
        dir, step = i[0], int(i[1:])
        if dir == "R":
            pos = (pos + step) % 100
        elif dir == "L":
            pos = (pos + 100 - step) % 100
        if pos == 0:
            cnt += 1
    return cnt


def part2(input):
    pos = 50
    cnt = 0
    for i in input:
        dir, step = i[0], int(i[1:])
        cnt += step // 100
        step = step % 100
        if dir == "R":
            new_pos = pos + step
            if pos != 0 and new_pos > 100:
                cnt += 1
            pos = new_pos % 100
        elif dir == "L":
            new_pos = pos - step
            if pos != 0 and new_pos < 0:
                cnt += 1
            pos = (new_pos + 100) % 100
        if pos == 0:
            cnt += 1
    return cnt