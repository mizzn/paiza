# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_minmax_boss
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    print(max(a), min(a))