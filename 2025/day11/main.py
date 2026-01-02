from collections import defaultdict


def parse(input):
    adjacent = defaultdict(set)
    for line in input:
        key, value = line.split(":")
        values = [v for v in value.split(" ") if v]
        adjacent[key].update(values)
    return adjacent


def dfs(dp, key, adjacent):
    if key not in dp:
        dp[key] = 0
        for neighbor in adjacent[key]:
            dp[key] += dfs(dp, neighbor, adjacent)
    return dp[key]


def part1(input):
    return dfs({"out": 1}, "you", parse(input))


def part2(input):
    parsed_input = parse(input)
    svr_dac = dfs({"dac": 1, "fft": 0}, "svr", parsed_input)
    dac_fft = dfs({"fft": 1}, "dac", parsed_input)
    fft_out = dfs({"out": 1, "dac": 0}, "fft", parsed_input)

    svr_fft = dfs({"fft": 1, "dac": 0}, "svr", parsed_input)
    fft_dac = dfs({"dac": 1}, "fft", parsed_input)
    dac_out = dfs({"out": 1, "fft": 0}, "dac", parsed_input)
    return svr_dac * dac_fft * fft_out + svr_fft * fft_dac * dac_out
