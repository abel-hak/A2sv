# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')
       
        
        for part in components:
            if part == "..":
                if stack: 
                    stack.pop()
            elif part and part != ".":  
                stack.append(part)
          
        
        return "/" + "/".join(stack)  
