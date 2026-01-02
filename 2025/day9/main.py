from collections import defaultdict
import bisect

def part1(input):
    cood = [[int(x) for x in n.split(",")] for n in input]
    res = 0
    for i in range(len(cood)):
        for j in range(i + 1, len(cood)):
            res = max(res, (abs(cood[i][0] - cood[j][0] + 1) * abs(cood[i][1] - cood[j][1] + 1)))
    return res


def merge_intervals(sorted_points):
    if not sorted_points:
        return []
    intervals = []
    s = sorted_points[0]
    e = s
    for p in sorted_points[1:]:
        if p == e + 1:
            e = p
        else:
            intervals.append((s, e))
            s = e = p
    intervals.append((s, e))
    return intervals


def part2(input):
    coords = []
    for item in input:
        if isinstance(item, (list, tuple)):
            coords.append([int(item[0]), int(item[1])])
        else:
            a, b = item.split(",")
            coords.append([int(a), int(b)])
    if not coords:
        return 0

    row_vals = defaultdict(list)
    col_vals = defaultdict(list)
    xmin, xmax = coords[0][0], coords[0][0]
    ymin, ymax = coords[0][1], coords[0][1]

    for x, y in coords:
        xmin, xmax = min(xmin, x), max(xmax, x)
        ymin, ymax = min(ymin, y), max(ymax, y)
        row_vals[y].append(x)
        col_vals[x].append(y)

    row_intervals = {}
    for y, xs in row_vals.items():
        xs_sorted = sorted(set(xs))
        row_intervals[y] = merge_intervals(xs_sorted)

    col_intervals = {}
    for x, ys in col_vals.items():
        ys_sorted = sorted(set(ys))
        col_intervals[x] = merge_intervals(ys_sorted)

    query_rows = set(row_vals.keys())
    row_vertical_xs = defaultdict(list)
    for x, intervals in col_intervals.items():
        for a, b in intervals:
            for y in list(query_rows):
                if a <= y <= b:
                    row_vertical_xs[y].append(x)
    for y in row_vertical_xs:
        row_vertical_xs[y].sort()

    query_cols = set(col_vals.keys())
    col_horizontal_ys = defaultdict(list)
    for y, intervals in row_intervals.items():
        for a, b in intervals:
            for x in list(query_cols):
                if a <= x <= b:
                    col_horizontal_ys[x].append(y)
    for x in col_horizontal_ys:
        col_horizontal_ys[x].sort()

    def find_left(xs_list, cur):
        if not xs_list:
            return None
        i = bisect.bisect_left(xs_list, cur)
        if i - 1 >= 0:
            return xs_list[i - 1]
        return None

    def find_right(xs_list, cur):
        if not xs_list:
            return None
        i = bisect.bisect_right(xs_list, cur)
        if i < len(xs_list):
            return xs_list[i]
        return None

    res = 0
    for x, y in coords:
        xs = row_vals[y]
        ys = col_vals[x]
        for nx in xs:
            for ny in ys:
                vx_list = row_vertical_xs.get(ny)
                left = find_left(vx_list, nx)
                if left is None:
                    continue
                right = find_right(vx_list, nx)
                if right is None:
                    continue
                hy_list = col_horizontal_ys.get(nx)
                up = find_left(hy_list, ny)
                if up is None:
                    continue
                down = find_right(hy_list, ny)
                if down is None:
                    continue
                width = right - left - 1
                height = down - up - 1
                if width > 0 and height > 0:
                    area = width * height
                    if area > res:
                        res = area
    return res
