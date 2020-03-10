def solution(m, n, puddles):
    maps = [[0] * (m+1) for _ in range(n+1)]
    maps[1][1] = 1

    for i in range(1, n+1):      # row
        for j in range(1, m+1):  # col
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                maps[i][j] = 0
            else:
                maps[i][j] += (maps[i][j-1] + maps[i-1][j]) % 1000000007
            # print(i, j, maps[i][j])
    return maps[n][m]

solution(4, 3, [[2, 2], [4,1]])