# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_kthmax_boss

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    a.sort(reverse=True)

    print(a[k-1])

