import re

class Solution:
    def simplifyPath(self, path: str) -> str:

        path1 = re.sub(r'/{2,}', '/', path)

        path2 = path1.split('/')
        path2[0] = 'root'

        path3 = [ p for p in path2 if p]

        stack = []

        for p in path3:
            if p == '..':
                if stack[-1] != 'root':
                    stack.pop()
            elif p == '.':
                continue
            else:
                stack.append(p)

        path4 = '/'.join(stack)

        return path4[4:] if path4 != 'root' else '/'




        