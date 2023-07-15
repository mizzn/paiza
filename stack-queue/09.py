# https://paiza.jp/works/mondai/stack_queue/stack_queue__practice_step3

from collections import deque

if __name__ == "__main__":
    n = int(input())
    a = list(map(str, input().split()))

    stack = deque()

    for i in range(n):
        if a[i]=='+':
            tmp2 = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp1 + tmp2)
        elif a[i]=='-':
            tmp2 = stack.pop()
            tmp1 = stack.pop()
            stack.append(tmp1 - tmp2)
        else:
            stack.append(int(a[i]))

    print(*stack)