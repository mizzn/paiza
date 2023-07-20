# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_value_step0

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    cnt = 0
    for i in range(n):
        if a[i] == k:
            cnt += 1

    print(cnt)