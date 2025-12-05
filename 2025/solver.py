import argparse
import importlib
import os
import sys


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Input file path")
    args = parser.parse_args()
    return args


def run(day, input_file):
    # Construct the module path (e.g., day1.main)
    module_name = f"{day}.main"

    # Construct the input file path (e.g., day1/input.txt)
    input_path = os.path.join(day, input_file)

    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    try:
        # Import the module dynamically
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found. Make sure {day}/main.py exists.")
        return

    # Read the input file
    lines = read_file(input_path)

    # Check if the module has parse_input, otherwise use raw lines
    if hasattr(module, "parse_input"):
        data = module.parse_input(lines)
    else:
        data = lines

    # Run Part 1
    if hasattr(module, "part1"):
        print(f"Part 1: {module.part1(data)}")
    else:
        print("Part 1: Not implemented (part1 or q1 function missing)")

    # Run Part 2
    if hasattr(module, "part2"):
        print(f"Part 2: {module.part2(data)}")
    else:
        print("Part 2: Not implemented (part2 or q2 function missing)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--day", type=str, required=True, help="The day folder (e.g., day1)")
    parser.add_argument("--input_file", type=str, required=True, help="The input file name (e.g., input.txt)")

    args = parser.parse_args()

    run(args.day, args.input_file)
