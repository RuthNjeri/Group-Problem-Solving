class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, path = [], path.split("/")
        
        for current in path:
            if stack and current == "..":
                stack.pop()
            elif current not in (".", "", ".."):
                stack.append(current)
                
        return "/" + "/".join(stack)
