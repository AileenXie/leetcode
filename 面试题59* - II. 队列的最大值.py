#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/7 10:46 AM
# @Author : aileen
# @File : 面试题59* - II. 队列的最大值.py
# @Software: PyCharm
"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5

"""


class MaxQueue:

    def __init__(self):
        self.max_v = []
        self.queue = []

    # TIME: O(1)
    def max_value(self) -> int:
        return self.max_v[0] if self.max_v else -1

    # TIME: O(1)
    # 而插入操作虽然看起来有循环，做一个插入操作时最多可能会有n
    # 次出队操作。但要注意，由于每个数字只会出队一次！！！，因此对于所有的n
    # 个数字的插入过程，对应的所有出队操作也不会大于n
    # 次。因此将出队的时间均摊到每个插入操作上，时间复杂度为O(1)
    def push_back(self, value: int) -> None:
        # 维护一个非升序的最大值序列
        # 当新插入value，在他之前的比他小的值都不会成为出栈时的最大值，可直接抛弃！
        if self.max_v:
            while self.max_v[-1] < value:
                del self.max_v[-1]
                if not self.max_v:
                    break
        self.max_v.append(value)
        self.queue.append(value)

    # TIME: O(1)
    def pop_front(self) -> int:
        if self.queue:
            pop_value = self.queue[0]
            del self.queue[0]
            if pop_value == self.max_v[0]:
                del self.max_v[0]
            return pop_value
        else:
            return -1


if __name__ == "__main__":
    obj = MaxQueue()
    result = [-1]

    def do_action(action, value):
        if action == "max_value":
            return obj.max_value()
        elif action == "push_back":
            obj.push_back(value[0])
            return None
        else:
            return obj.pop_front()

    actions = ["MaxQueue", "max_value", "pop_front", "max_value", "push_back", "max_value", "pop_front", "max_value", "pop_front",
     "push_back", "pop_front", "pop_front", "pop_front", "push_back", "pop_front", "max_value", "pop_front",
     "max_value", "push_back", "push_back", "max_value", "push_back", "max_value", "max_value", "max_value",
     "push_back", "pop_front", "max_value", "push_back", "max_value", "max_value", "max_value", "pop_front",
     "push_back", "push_back", "push_back", "push_back", "pop_front", "pop_front", "max_value", "pop_front",
     "pop_front", "max_value", "push_back", "push_back", "pop_front", "push_back", "push_back", "push_back",
     "push_back", "pop_front", "max_value", "push_back", "max_value", "max_value", "pop_front", "max_value",
     "max_value", "max_value", "push_back", "pop_front", "push_back", "pop_front", "max_value", "max_value",
     "max_value", "push_back", "pop_front", "push_back", "push_back", "push_back", "pop_front", "max_value",
     "pop_front", "max_value", "max_value", "max_value", "pop_front", "push_back", "pop_front", "push_back",
     "push_back", "pop_front", "push_back", "pop_front", "push_back", "pop_front", "pop_front", "push_back",
     "pop_front", "pop_front", "pop_front", "push_back", "push_back", "max_value", "push_back", "pop_front",
     "push_back", "push_back", "pop_front"]
    values = [[], [], [], [], [46], [], [], [], [], [868], [], [], [], [525], [], [], [], [], [123], [646], [], [229], [], [],
     [], [871], [], [], [285], [], [], [], [], [45], [140], [837], [545], [], [], [], [], [], [], [561], [237], [],
     [633], [98], [806], [717], [], [], [186], [], [], [], [], [], [], [268], [], [29], [], [], [], [], [866], [],
     [239], [3], [850], [], [], [], [], [], [], [], [310], [], [674], [770], [], [525], [], [425], [], [], [720], [],
     [], [], [373], [411], [], [831], [], [765], [701], []]

    for action, values in zip(actions[1:], values[1:]):
        ans = do_action(action,values)
        result.append(ans)
    print(result)

