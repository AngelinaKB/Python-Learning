# indexing = accessing elements of a sequence using []
# [start : end : step]

credit_number = "1234-5678-9012-3456"
print(f"\nThe character at index 4 is: {credit_number[4]}")
print(f"The first 4 digits of your credit card are: {credit_number[:4]}")
print(f"The last 4 digits of your credit card are: {credit_number[-4 :]}")
print(f"Your shortened credit card number is: {credit_number[::3]}")

credit_number = "1234-5678-9012-3456"
last_digits= credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")