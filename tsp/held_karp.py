import sys
from itertools import combinations

from input import read_adjacency_matrix


def held_karp(dists: list[list[int]]):
    n = len(dists)
    cost = {}

    for i in range(1, n):
        cost[(1 << i, i)] = (dists[0][i], 0)

    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for i in subset:
                prev_bits = bits & ~(1 << i)
                result = []
                for m in subset:
                    if m == 0 or m == i:
                        continue
                    result.append((cost[(prev_bits, m)][0] + dists[m][i], m))
                cost[(bits, i)] = min(result)

    result = []
    bits = (2**n - 1) - 1
    for i in range(1, n):
        result.append((cost[(bits, i)][0] + dists[i][0], i))

    optimal, parent = min(result)

    path = []
    for _ in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = cost[(bits, parent)]
        bits = new_bits

    return optimal, [0] + path[::-1] + [0]


if __name__ == "__main__":
    cost, path = held_karp(read_adjacency_matrix(sys.stdin))
    print(f"Cost: {cost}\nPath: {path}")
