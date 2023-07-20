# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_condition_step6

if __name__ == "__main__":
    n = int(input())
    names = []
    scores_int = []
    for i in range(n):
        nametmp, scoretmp_str = input().split()
        names.append(nametmp)
        scores_int.append(int(scoretmp_str))
    k = int(input())

    for i in range(n):
        if scores_int[i] >= k:
            print(names[i])

