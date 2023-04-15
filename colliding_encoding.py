import sys
from typing import List, Tuple

def colliding_encoding(T: int, test_cases: List[Tuple[List[str], int, List[str]]]) -> List[str]:
    result = []
    for t, (D, N, S) in enumerate(test_cases, 1):
        encoded_words = set()
        collision = False
        for word in S:
            encoded_word = ''.join(D[ord(c) - ord('A')] for c in word)
            if (encoded_word in encoded_words):
                collision = True
                break
            else:
                encoded_words.add(encoded_word)
        result.append(f"Case #{t}: {'YES' if collision else 'NO'}")
    
    return result

def main():
    T = int(sys.stdin.readline().rstrip())
    test_cases = []

    for _ in range(T):
        D = sys.stdin.readline().rstrip().split()
        N = int(sys.stdin.readline().rstrip())
        S = [sys.stdin.readline().rstrip() for _ in range(N)]
        test_cases.append((D, N, S))

    results = colliding_encoding(T, test_cases)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
