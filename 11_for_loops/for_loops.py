# for = execute block of code in a fixed number of times. 

# print numbers 1-10
for x in range(1,11):
    print(x, end=" ")

# print reversed numbering 10-1
for x in reversed(range(1,11)):
    print(x,end=" ")

# print numbers 1-10 with a step of 2
for x in range(1,11,2):
    print(x,end=" ")

# loop over string
credit_number = "1234-5678-9102-3456"
for x in credit_number:
    print(x, end="")

# continue keyword allows you to pass over certain values
for x in range(1,21):
  if x == 13:
    continue
  else:
    print(x, end=" ")

# break keyword allows you to exit out when certain condition is met
for x in range(1,21):
  if x == 13:
    break
  else:
    print(x, end=" ")