from multi_bracket_validation import multi_bracket_validation

# is_balanced.py ?


def is_balanced(string):
    return multi_bracket_validation(string)
# multi_bracket_validation.py


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
    if len(stack) > 0:
        return False
    else:
        return True
