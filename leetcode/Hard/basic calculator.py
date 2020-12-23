# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num = 0
        ret = 0
        sign = 1
        
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            
            if c == '+' or c == '-':
                ret += num * sign
            
                sign = 1
                if c == '-':
                    sign = -1
                
                num = 0
                
            if c == '(':
                stack.append(ret)
                stack.append(sign)
                
                sign = 1
                ret = 0
                
            if c == ')':
                ret += sign * num
                
                ret *= stack.pop()
                ret += stack.pop()
                num = 0
                
        return ret + sign * num
