# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_condition_step0
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i]%2==0:
            print(i+1)
            break