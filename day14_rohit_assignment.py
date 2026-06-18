# ==========================================
# Question 1: Build Your Own Stack
# ==========================================

stack = []

def push(item):
    stack.append(item)
    print(f"Pushed {item} -> {stack}")

def pop():
    if len(stack) == 0:
        print("Stack is Empty")
        return None

    item = stack.pop()
    print(f"Popped {item} -> {stack}")
    return item

def peek():
    if len(stack) == 0:
        print("Stack is Empty")
        return None

    return stack[-1]


print("===== Question 1: Stack Operations =====")

push(1)
push(2)
push(3)
push(4)

print("Top Element:", peek())

pop()
pop()

print("Final Stack:", stack)


# ==========================================
# Question 2: Balanced Parentheses Checker
# ==========================================

def is_balanced(expression):

    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expression:

        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":

            if len(stack) == 0:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0


print("\n===== Question 2: Balanced Parentheses =====")

test_cases = [
    "{[()()]}",
    "{[(])}",
    "((()))",
    "[{()}]()"
]

for expression in test_cases:

    if is_balanced(expression):
        print(f"{expression} -> Balanced")
    else:
        print(f"{expression} -> Not Balanced")