# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_condition_step4

if __name__ == "__main__":
    n = int(input())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    k = int(input())
    # print(x)
    # print(p)

    ans = 0
    for i in range(n):
        d = abs(x[i][0] - x[n-1][0]) + abs(x[i][1] - x[n-1][1])
        if d <= k:
            ans += 1

    print(ans)
