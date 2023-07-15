# https://paiza.jp/works/mondai/stack_queue/stack_queue__practice_step2

from collections import deque

if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    oldsum = sum(a[:x]) # 0~x-1までの合計
    maxsum = oldsum
    L = a[0]

    for i in range(x, n):
        nowsum = oldsum - a[i - x] + a[i]
        if maxsum < nowsum:
            maxsum = nowsum
            L = a[i - x + 1]
        oldsum = nowsum

    print(maxsum, L)