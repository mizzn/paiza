# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_value_step1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    ans = 0
    for i in range(n):
        if a[i] == k:
            ans = i
            break
    if ans == 0:
        print(ans)
    else:
        print(ans+1)