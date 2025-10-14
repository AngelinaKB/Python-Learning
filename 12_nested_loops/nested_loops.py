# nested loops =  A loop withing another loop
#                 outer loop:
#                   inner loop:

# prints 1-10, 3 times
for x in range(3):
    for y in range(1,11):
        print(y, end="")
        if y<10:
          print("-",end="")
    print()


# Generate a rectangle 
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
  for y in range(columns):
    print(symbol, end="")
  print()