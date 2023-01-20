
def climb_stair(n):
    F = [1]*(n+1)

    for i in range(2, n + 1):
        F[i] = F[i-1] + F[i-2]
    return F[-1]


if __name__ == "__main__":
    print(climb_stair(10))
    print(climb_stair(20))
    print(climb_stair(30))

