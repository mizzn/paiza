# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_kthmax_step0

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    print(a[-2])

