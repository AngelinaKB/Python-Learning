# membership operator =  used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                         1. in
#                         2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter.capitalize() in word:
    print(f"There is a {letter}!")
    
else:
    print(f"{letter} was not found!")
    
    
students =  {"Amy", "Jack" , "Sandy"}

search_student_name = input("Enter the name of the student: ")

if search_student_name in search_student_name:
    print(f"{search_student_name} is in student list.")

else:
    print(f"{search_student_name} not found.")
    

grades = {"Sandy": "A",
          "Amy": "B",
          "Jack" : "C"}
student = input("Enter the name of a student: ").capitalize()

if student in grades:
    print(f"Students grade is {grades[student]}")
    
else:
    print(f"{student} was not found.")
    
    
# check for valid email

email = "testemail@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
    
else:
    print("Invalid email.")
