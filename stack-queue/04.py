# https://paiza.jp/works/mondai/stack_queue/stack_queue__stack_step2

from collections import deque

if __name__ == "__main__":
    n = int(input())
    query = []

    for _ in range(n):
        query.append(list(map(str, input().split())))
    # print(a)
    stack = deque()

    for q in query:
        if q[0] == '1':
            # 1のときpush
            stack.append(q[1]) # 右からいれて
        elif q[0] == '2':
            # 2のときpop
            print(stack.pop()) # 右から出す
        else:
            print("ERROR!")
            exit(0)
        
        
        print(*stack)
    
