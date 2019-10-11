def is_matched(expression):
    if len(expression) % 2 != 0:
        return False

    opening = ("(", "[", "{")
    closing = (")", "]", "}")
    mapping = {opening[0]:closing[0],
               opening[1]:closing[1],
               opening[2]:closing[2]}

    if expression[0] in closing:
        return False

    if expression[-1] in opening:
        return False

    closing_queue = []
    for letter in expression:
        if letter in opening:
            closing_queue.append(mapping[letter])
        elif letter in closing:
            if not closing_queue:
                return False

            if closing_queue[-1] == letter:
                closing_queue.pop()
            else:
                return False

    return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
