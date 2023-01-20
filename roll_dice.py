
def roll_dice(N,M):
    F = [[0]*M]*N
    F[0] = [1]*6 + [0]*(M-6)

    for i in range(1, N):
        for j in reversed(range(M)):
            F[i][j] = 0  # This doesn't make any sense, but it won't work without it
            for k in range(1, 7):
                if j - k >= 0:
                    F[i][j] += F[i - 1][j - k]

    return F[-1][-1]


if __name__ == "__main__":
    print(roll_dice(2,7))
    print(roll_dice(3,9))
    print(roll_dice(8,24))
