# logical operators = evaluate multiple conditions (or, and, not)
#       or = at least one condition must be True
#       and = both conditions must be True
#       not = invert the conditions (not False, not True)

# or
temp = 25
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scehduled")

# and
temp = 25
is_sunny= True

if temp>=28 and is_sunny:
    print("It is hot outside and sunny.")
elif temp<=0 and is_sunny:
    print("It is cold outside and sunny.")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside and sunny.")

# not
is_student = False

if not is_student:
    print("you're not a student")
