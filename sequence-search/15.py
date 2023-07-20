# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_condition_boss

if __name__ == "__main__":
    n = int(input())
    names = []
    scores = []
    for i in range(n):
        name, scorestr = input().split()
        names.append(name)
        scores.append(int(scorestr))
    k, l = map(int, input().split())

    for i in range(n):
        if k <= scores[i] and scores[i] <= l:
            print(names[i])
            

