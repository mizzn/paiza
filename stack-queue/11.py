# https://paiza.jp/works/mondai/stack_queue/stack_queue__practice_step5

from collections import deque

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    queue = deque()
    for i in range(k):
        queue.append(0) # 人がいないとき0

    T = a[-1]+1
    i = 0
    for t in range(1, T):
        #先頭を下ろす
        queue.popleft()
        if t == a[i]:
            queue.append(1)
            i += 1
            print(sum(queue))
        else:
            queue.append(0)