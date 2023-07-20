# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_condition_step3
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    ans = -101

    for i in range(n):
        if a[i]<=k:
            if ans < a[i]:
                ans = a[i]

    print(ans)