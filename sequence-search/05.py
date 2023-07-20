# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_minmax_step0

if __name__ == "__main__":
    a1, a2 = map(int, input().split())

    if a1 < a2:
        print(a2, a1)
    else:
        print(a1, a2)