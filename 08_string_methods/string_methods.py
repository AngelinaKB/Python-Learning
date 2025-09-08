# Sample string
text = "  Hello World 123  "

print("Original:", repr(text))

# 1. Case Conversion
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())

# 2. Searching & Checking
print("Find 'o':", text.find("o"))
print("Count 'l':", text.count("l"))
print("Startswith 'He':", text.strip().startswith("He"))
print("Endswith '123':", text.strip().endswith("123"))

# 3. Validation
print("Is Alpha:", "Hello".isalpha())
print("Is Digit:", "123".isdigit())
print("Is Alnum:", "Hello123".isalnum())
print("Is Space:", "   ".isspace())
print("Is Lower:", "hello".islower())
print("Is Upper:", "HELLO".isupper())
print("Is Title:", "Hello World".istitle())

# 4. Modifying Strings
print("Strip:", text.strip())
print("LStrip:", text.lstrip())
print("RStrip:", text.rstrip())
print("Replace 'World' -> 'Python':", text.replace("World", "Python"))

# 5. Splitting & Joining
print("Split:", text.split())
print("Split by 'o':", text.split("o"))
print("Join with '-':", "-".join(["a", "b", "c"]))


