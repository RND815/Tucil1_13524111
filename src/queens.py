from collections import defaultdict
from itertools import product
import time
import sys

def load_board(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f]

def save_board(board, queens):
    with open("test/output.txt", "w") as f:
        size = len(board)
        for r in range(size):
            row = ""
            for c in range(size):
                if (r, c) in queens:
                    row += "#"
                else:
                    row += board[r][c]
            f.write(row.strip() + "\n")

def build_regions(board):
    regions = defaultdict(list)
    n = len(board)
    for r in range(n):
        for c in range(n):
            regions[board[r][c]].append((r, c))
    return regions

def is_valid(positions):
    for i in range(len(positions)):
        r1, c1 = positions[i]
        for j in range(i + 1, len(positions)):
            r2, c2 = positions[j]
            if r1 == r2:
                return False
            if c1 == c2:
                return False
            if abs(r1 - r2) == abs(c1 - c2):
                return False
    return True

def print_board(board, queens):
    n = len(board)
    for r in range(n):
        row = ""
        for c in range(n):
            if (r, c) in queens:
                row += "#"
            else:
                row += board[r][c]
        print(row)
    print()

def main():
    if len(sys.argv) != 2:
        print("Format input salah")
        return
    board = load_board(sys.argv[1])
    regions = build_regions(board)
    region_lists = list(regions.values())

    iteration = 0
    solution = None

    start = time.perf_counter()
    last_print_time = start

    for combination in product(*region_lists):
        iteration += 1
        now = time.perf_counter()

        if now - last_print_time >= 0.3:
            print(f"\nKombinasi ke-{iteration}")
            print_board(board, combination)
            last_print_time = now

        if is_valid(combination):
            solution = combination
            break

    end = time.perf_counter()

    print("\n======================")
    if solution:
        print("Solusi ditemukan:")
        print_board(board, solution)
        save_board(board, solution)
    else:
        print("Solusi tidak ditemukan!")

    print("Total kombinasi yang dicek:", iteration)
    print("Waktu pencarian:", round((end - start) * 1000, 3), "ms")

if __name__ == "__main__":
    main()