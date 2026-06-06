class Solution:
    def isValid(self, s: str) -> bool:
        open_paran = [ "(", "[", "{"]
        close_paran = [")", "]",  "}"]
        stack = []
        for character in s:
            if character in open_paran : 
                stack.append(character)
            elif character in close_paran:
                if len(stack) == 0:
                    return False
                bracket_index = close_paran.index(character)
                matching_open_bracket = open_paran[bracket_index]
                if stack[-1] == matching_open_bracket:
                    stack.pop()
                else:
                    return False
        return len(stack) ==0 

        