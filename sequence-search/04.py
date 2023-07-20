# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_value_boss

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    for i in range(n):
        if a[i] == k:
            print(i+1)