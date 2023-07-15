# https://paiza.jp/works/mondai/stack_queue/stack_queue__common_step1

from collections import deque

if __name__ == "__main__":
    q = deque()

    n = int(input())
    for _ in range(n):
        # 右からいれて
        q.append(int(input()))

    print(n)
    for _ in range(n):
        # 左から出す
        print(q.popleft())