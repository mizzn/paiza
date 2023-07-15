# https://paiza.jp/works/mondai/stack_queue/stack_queue__queue_step1

from collections import deque

if __name__ == "__main__":
    n = int(input())
    query = []

    for _ in range(n):
        query.append(list(map(str, input().split())))
    # print(a)
    queue = deque()

    for q in query:
        if q[0] == '1':
            # 1のときpush
            queue.append(q[1]) # 右からいれて
        elif q[0] == '2':
            # 2のときpop
            queue.popleft() # 左から出す
        else:
            print("ERROR!")
            exit(0)
        
        print(*queue)