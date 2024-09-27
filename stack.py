s="()[]"
stack=[]
is_valid=True
for char in s:
  if char in brackets.values():
    stack.append(char)
  elif char in bracket.keys():
    if stack and stack[-1]==brackets[char]:
        stack.pop()
    else:
        is_valid=false
        break
if is_valid and not stack:
    print(true)
else:
    print(false)
