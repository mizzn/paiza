# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_value_step2

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    ans = n
    for i in range(n-1, -1, -1):
        if a[i] == k:
            ans = i
            break
    if ans == n:
        print(0)
    else:
        print(ans+1)