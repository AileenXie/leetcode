#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/2 8:25 AM
# @Author : aileen
# @File : 150_evaluate_reverse_polish_notation.py
# @Software: PyCharm

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


class Solution:
    def operate(self, symbol, num1, num2):
        if symbol == "+":
            return num1 + num2
        if symbol == "-":
            return num1 - num2
        if symbol == "*":
            return num1 * num2
        if symbol == "/":
            return int(num1 / num2)   # !!! 包括负数的向零取整不能用//

    def isnumber(self, string):
        try:
            num = int(string)
            return isinstance(num, int)
        except ValueError:
            return False

    def evalRPN(self, tokens) -> int:
        if len(tokens) == 0:
            return None
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for char in tokens:
            if self.isnumber(char):
                stack.append(int(char))
            else:
                pre_num = stack[-1]
                del stack[-1]
                last_result = stack[-1]
                del stack[-1]
                last_result = self.operate(char, last_result, pre_num)  # 不进栈，读数的次序会有问题
                stack.append(last_result)
        return last_result


if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    tokens = ["18"]
    print(Solution().evalRPN(tokens))
