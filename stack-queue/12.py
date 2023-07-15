# https://paiza.jp/works/mondai/stack_queue/stack_queue__practice_step6

from collections import deque

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    stack = deque()
    for i in range(n):
        stack.append(a[i]) # 1個追加

        while len(stack)>=2:
            #要素が2個以上のとき，右の2個を比べる
            tmp1 = stack.pop() # 一番右
            tmp2 = stack.pop() # 二番目に右
            if tmp1 == tmp2:
                # 同じだったら2倍にして戻す
                stack.append(tmp1*2)
            else:
                # 違かったらもとに戻してwhileから逃げる
                stack.append(tmp2)
                stack.append(tmp1)
                break

        
    while stack:
        print(stack.pop())
