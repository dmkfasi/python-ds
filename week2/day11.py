def count_invalid_parenthesis(string):
  # Fill this in.

  # Define open and closing patenthesis to lookup for
  b_open, b_close = '(', ')'
  # Counters for each kind of parenthesis
  open_cnt, close_cnt = 0, 0

  # Convert input string into a List
  stack = list(string)
  # Reverse the List to pop from the beginning
  stack.reverse()

  # Pop out charaters one by one and count each parenthesis
  while stack:
    c = stack.pop()

    # Update parenthesis counters accordingly
    if c == b_open:
      open_cnt += 1
    if c == b_close:
      close_cnt += 1

  # Absolute difference between amount of parenthesis is the outcome solution
  return abs(open_cnt - close_cnt)

print(count_invalid_parenthesis("()())()"))
# 1

print(count_invalid_parenthesis(")("))
# 0

print(count_invalid_parenthesis(")()))((()))"))
# 3
