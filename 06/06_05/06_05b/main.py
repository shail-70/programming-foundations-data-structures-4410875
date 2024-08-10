
def check_matching_parentheses(str):
  stk = []
  for c in str:
    if c == "(":
      stk.append(c)
    elif c == ")":
      if len(stk) == 0:
        return False
      elif "(" != stk.pop():
        return False
  if len(stk) == 0:
    return True
  else:
    return False
    
print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))
print(check_matching_parentheses("())"))
print(check_matching_parentheses("((())"))