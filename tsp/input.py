from typing import Iterable


def read_adjacency_matrix(source: Iterable[str]) -> list[list[int]]:
    matrix = []
    for line in source:
        matrix.append(list(map(int, line.split())))

    assert all(len(row) == len(matrix) for row in matrix), "invalid adjacency matrix"

    return matrix
