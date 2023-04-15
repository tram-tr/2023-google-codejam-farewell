import sys
from collections import defaultdict
from typing import List, Tuple

def group_colors(S: List[int]) -> List[List[int]]:
    groups = []
    current_group = [S[0]]

    for i in range(1, len(S)):
        if (S[i] != S[i - 1]):
            groups.append(current_group)
            current_group = [S[i]]
        else:
            current_group.append(S[i])

    groups.append(current_group)
    return groups

def process_case(N: int, S: List[int]) -> str:
    grouped_colors = group_colors(S)
    color_assignments = {}
    prev_color = grouped_colors[0][0]
    color_assignments[prev_color] = 1
    current_int = 2

    for group in grouped_colors[1:]:
        current_color = group[0]
        if (current_color != prev_color):
            color_assignments[current_color] = current_int
            current_int += 1
        else:
            color_assignments[current_color] = color_assignments[prev_color]
        prev_color = current_color

    if any(color_assignments[S[i]] > color_assignments[S[i+1]] for i in range(N-1)):
        return "IMPOSSIBLE"

    color_order = " ".join(str(color) for color in sorted(color_assignments.keys(), key=lambda x: color_assignments[x]))
    return color_order

def rainbow_sort(T: int, test_cases: List[Tuple[int, List[int]]]) -> List[str]:
    results = []

    for t, (N, S) in enumerate(test_cases, 1):
        color_order = process_case(N, S)
        results.append(f"Case #{t}: {color_order}")

    return results

def main():
    T = int(sys.stdin.readline().rstrip())
    test_cases = []

    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        S = list(map(int, sys.stdin.readline().rstrip().split()))
        test_cases.append((N, S))

    results = rainbow_sort(T, test_cases)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
