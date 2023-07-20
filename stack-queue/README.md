# stack-queue
[スタック・キューメニュー](https://paiza.jp/works/mondai/stack_queue/problem_index?language_uid=python3)
## deque
両端キューとして便利
- [英語](https://wiki.python.org/moin/TimeComplexity)
- [日本語](https://note.nkmk.me/python-collections-deque/)
> リストは先頭の要素に対する削除や追加（挿入）の処理速度が遅いためdequeのほうが効率的。
> なお、dequeには、両端以外の要素へのアクセスが遅いというデメリットもあるので注意。

## dequeの使い方
インポート：`from collections import deque`
オブジェクトを生成：`deque()`
右から追加：`append()`
左から追加：`appendleft()`
右から取り出す：`pop()`
左から取り出す：`popleft()`

途中に要素を追加：`insert(位置, 追加する値)`
削除：`remove(削除したい値)`
    削除したい値が複数あるときは最初の要素が削除
空にする：`clear()`