import sys
from typing import List, Tuple

def illumination_optimizing(T: int, test_cases: List[Tuple[int, int, int, List[int]]]) -> List[str]:
    result = []

    for t, (M, R, N, X) in enumerate(test_cases, 1):
        bulbs = 0
        i = 0
        left = 0

        while (left < M):
            right = left
            while (i < N and X[i] - R <= left):
                right = max(right, X[i] + R)
                i += 1
            if left == right:
                result.append(f"Case #{t}: IMPOSSIBLE")
                break
            bulbs += 1
            left = right
        else:
            result.append(f"Case #{t}: {bulbs}")
        

    return result

def main():
    T = int(sys.stdin.readline().rstrip())
    test_cases = []

    for _ in range(T):
        M, R, N = map(int, sys.stdin.readline().rstrip().split())
        X = list(map(int, sys.stdin.readline().rstrip().split()))
        test_cases.append((M, R, N, X))

    results = illumination_optimizing(T, test_cases)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
