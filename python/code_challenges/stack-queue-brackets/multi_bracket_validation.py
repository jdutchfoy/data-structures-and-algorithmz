def multi_bracket_validation(string):
    stack = []
    for char in string:
        if char in ['{', '[', '(']:
            stack.append(char)
        elif char in ['}', ']', ')']:
            if len(stack) == 0:
                return False
            else:
                most_recent_opening = stack.pop()
                if (char == '}' and most_recent_opening != '{') or \
                   (char == ']' and most_recent_opening != '[') or \
                   (char == ')' and most_recent_opening != '('):
                    return False
    if len(stack) <= 0:
        return True
    else:
        return False
