from collections import defaultdict
from queue import PriorityQueue

# These variables stand for ; T: the is the total number of test cases, N is the total number of nodes and the vertices
# M is written as two variables which are x and y, which are aby 2 nodes, and it has a third variable which is
# the weight of the vertex, and lastly S is the starting node/ the source
T, N, M, G, S = None, None, None, None, None


def read_test():
    # this function will firstly load all the variables for one specific test case

    global N, M, G, S
    # the program will then create a dictionary for the total number of nodes with the details of how they are
    # connected and the associated weights

    N, M = map(int, input().split())
    G =  (lambda: {})
    for _ in range(M):
        x, y, c = map(int, input().split())
        x, y = x - 1, y - 1
        if y in G[x]:
            c = min(c, G[x][y])
        G[x][y] = c
        G[y][x] = c
    S = int(input()) - 1


def solve_test():
    global N, M, S, G
    Q = PriorityQueue(N * N)
    Q.put((0, S))
    D = [-1] * N
    D[S] = 0

    while not Q.empty():
        cost, x = Q.get()
        for y in G[x]:
            if D[y] == -1 or D[y] > D[x] + G[x][y]:
                D[y] = D[x] + G[x][y]
                Q.put((D[y], y))

    D.pop(S)
    return D


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        read_test()
        sol = solve_test()
        print(' '.join(map(str, sol)))