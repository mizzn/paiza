# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_condition_step5

if __name__ == "__main__":
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    xs, xt = map(int, input().split())
    ys, yt = map(int, input().split())
    
    ans = 0
    for i in range(n):
        if xs <= p[i][0] and p[i][0] <= xt and ys <= p[i][1] and p[i][1] <= yt:
            ans += 1

    print(ans)
