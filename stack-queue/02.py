# https://paiza.jp/works/mondai/stack_queue/stack_queue__common_step2

from collections import deque

if __name__ == "__main__":
    n = int(input())
    query = []

    for _ in range(n):
        query.append(list(map(int, input().split())))
    # print(a)
    a = deque()

    for q in query:
        if q[0] == 1:
            # 1のときpush
            a.append(q[1])
        elif q[0] == 2:
            continue
        else:
            print("ERROR!")
            exit(0)

    print(len(a))
    for _ in range(len(a)):
        print(a.popleft())
