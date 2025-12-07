def part1(input):
    nums = []
    for i in input[:-1]:
        nums.append([int(num) for num in i.split() if num != " "])
    ops = [n for n in input[-1] if n != " "]
    r, c = len(nums), len(nums[0])
    res = 0
    for j in range(c):
        col_res = 0 if ops[j] == "+" else 1
        for i in range(r):
            if ops[j] == "+":
                col_res += nums[i][j]
            elif ops[j] == "*":
                col_res *= nums[i][j]
        res += col_res
    return res


def part2(input):
    nums = []
    ops = []
    temp_nums = []

    for i in range(len(input[0])):
        n_str = ""
        cnt = 0
        for j in range(len(input) - 1):
            n_str += input[j][i]
            if input[j][i] == " ":
                cnt += 1

        if input[-1][i] != " ":
            ops.append(input[-1][i])
        if cnt == len(input) - 1:
            nums.append(temp_nums)
            temp_nums = []
        else:
            temp_nums.append(int(n_str))
    nums.append(temp_nums)
    res = 0
    for i in range(len(ops)):
        res_temp = 0 if ops[i] == "+" else 1
        for j in range(len(nums[i])):
            if ops[i] == "+":
                res_temp += nums[i][j]
            elif ops[i] == "*":
                res_temp *= nums[i][j]
        res += res_temp
    return res
