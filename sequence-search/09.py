# https://paiza.jp/works/mondai/sequence_search_problems/sequence_search_problems_search_condition_step1
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-1, -1, -1):
        if a[i]%2==1:
            print(i+1)
            break