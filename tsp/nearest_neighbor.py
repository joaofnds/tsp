import sys

from input import read_adjacency_matrix


def nearest_neighbor(dists: list[list[int]]):
    unvisited = list(range(1, len(dists)))
    tour = [0]
    while unvisited:
        nearest = min(unvisited, key=lambda i: dists[tour[-1]][i])
        tour.append(nearest)
        unvisited.remove(nearest)
    tour.append(0)
    return sum(dists[tour[i]][tour[i + 1]] for i in range(len(dists))), tour


if __name__ == "__main__":
    cost, path = nearest_neighbor(read_adjacency_matrix(sys.stdin))
    print(f"Cost: {cost}\nPath: {path}")
