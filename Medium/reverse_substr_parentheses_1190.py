class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ch = ""

        for st in s:
            if st == '(':
                stack.append(ch)
                ch = ""
            elif st == ')':
                ch = ch[::-1]
                if stack:
                    ch = stack.pop() + ch
            else:
                ch += st

        return ch

    def reverseParentheses2(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        # First pass: Pair up parentheses
        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        # Second pass: Build the result string
        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction

        return "".join(result)


obj = Solution()
s = "(ed(et(oc))el)"
print(obj.reverseParentheses2(s))
