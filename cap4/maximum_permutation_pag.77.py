def naive_max_permutation(M, A=None):
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_permutation(M, A)
    return A


M = [2, 2, 0, 5, 3, 5, 7, 4]
print(naive_max_permutation(M))


def max_perm(M):
    n = len(M)
    A = set(range(n))
    count = [0]*n
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A


print(max_perm(M))


def naive_celebrity(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v]:
                break
            if not G[v][u]:
                break
        else:
            return u
    return None


from random import randrange
n = 100
G = [[randrange(2) for i in range(n)] for i in range(n)]
c = randrange(n)
for i in range(n):
    G[i][c] = True
    G[c][i] = False

print(naive_celebrity(G))
