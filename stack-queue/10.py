# https://paiza.jp/works/mondai/stack_queue/stack_queue__practice_step4

from collections import deque

if __name__ == "__main__":
    n = int(input())
    s = input()

    stack = deque()
    for i in range(n):
        if s[i]=='(':
            stack.append(s[i])
        elif s[i]==')':
            if len(stack)==0:
                print("No")
                exit(0)
            stack.pop()
        else:
            print("ERROR")
            exit(-1)

    if len(stack)==0:
        print("Yes")
    else:
        print("No")