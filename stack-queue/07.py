# https://paiza.jp/works/mondai/stack_queue/stack_queue__practice_step1

from collections import deque

if __name__ == "__main__":
    n = int(input())
    query = []

    for _ in range(n):
        query.append(list(map(str, input().split())))
    # print(a)
    queue1 = deque()
    queue2 = deque()

    for q in query:
        if q[0] == '1':
            # push
            if q[1] == '1':
                # push1
                queue1.append(q[2])
            elif q[1] == '2':
                # push2
                queue2.append(q[2])
            else:
                print("PUSH ERROR")
                exit(0)
        elif q[0] == '2':
            # pop
            if q[1] == '1':
                # pop1
                print(queue1.popleft())
            elif q[1] == '2':
                # push2
                print(queue2.popleft())
            else:
                print("POP ERROR")
                exit(0)
        elif q[0] == '3':
            # size
            print(len(queue1), len(queue2))
        else:
            print("ERROR!")
            exit(0)
        
    
