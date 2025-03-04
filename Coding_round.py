'''
Coding Round @Simform on 4th March, 2025 - 

We were asked to solve any one out of 2 questions in an hour.

I was able to solve 1st within 45 mins. Wasted lot of time in bad approach. But it helped me to come up with recursive one in minutes.

After that I started solving the second one. I was able to solve it in 30 mins along with the right approach from the start.
'''


# Question - 1 (https://leetcode.com/problems/integer-to-roman/description/)

from typing import List

## Better approach 
class Solution:
    def intToRoman(self, num: int) -> str:
        i_2_r = {0: '', 1: 'I', 4: 'IV', 5: 'V', 9:'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        def intToRomanRecursive(num, i,  roman):
            if num == 0:
                return roman
            if num >= base[i]:
                power =  num // base[i]
                num %= base[i]
                roman += (power * i_2_r[base[i]])
            return intToRomanRecursive(num, i + 1, roman)

        return intToRomanRecursive(num, 0, '')


## Very bad approach 
class Solution:
    def intToRoman(self, num: int) -> str:
        i_2_r = {0: '', 1: 'I', 4: 'IV', 5: 'V', 9:'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        while num > 0:
            if num >= 1000:
                power =  num // 1000
                num %= 1000
                roman += (power * i_2_r[1000])
            if num >= 900:
                power =  num // 900
                num %= 900
                roman += (power * i_2_r[900])
            if num >= 500:
                power =  num // 500
                num %= 500
                roman += i_2_r[500]
            if num >= 400:
                power =  num // 400
                num %= 400
                roman += (power * i_2_r[400])
            if num >= 100:
                power =  num // 100
                num %= 100
                roman += (power * i_2_r[100])
            if num >= 90:
                power =  num // 90
                num %= 90
                roman += (power * i_2_r[90])
            if num >= 50:
                power =  num // 50
                num %= 50
                roman += i_2_r[50]
            if num >= 40:
                power =  num // 40
                num %= 40
                roman += (power * i_2_r[40])
            if num >= 10:
                power =  num // 10
                num %= 10
                roman += (power * i_2_r[10])
            if num >= 9:
                power =  num // 9
                num %= 9
                roman += (power * i_2_r[9])
            if num >= 5:
                power =  num // 5
                num %= 5
                roman += i_2_r[5]
            if num >= 4:
                power =  num // 4
                num %= 4
                roman += (power * i_2_r[4])
            if num >= 1:
                power =  num // 1
                num %= 1
                roman += (power * i_2_r[1])
        return roman


# Question - 2 (https://leetcode.com/problems/all-paths-from-source-to-target/)

## Using Backtracking 
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        stack = [0]
        def backtrack(i, last):
            if i == last:
                paths.append(list(stack))
                return
            for adj in graph[i]:
                stack.append(adj)
                backtrack(adj, last)
                stack.pop()
            return 
        backtrack(0, len(graph) - 1)
        return paths
