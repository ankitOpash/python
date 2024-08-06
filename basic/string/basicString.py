#moslty in same in string like decalartion 

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])
print(len(a))

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"

print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

print("expensive" not in txt)

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


  a = "  Hello, World!"
print(a.upper())

# The strip() method removes any whitespace from the beginning or the end:

print(a.strip()) 

# The replace() method replaces a string with another string:
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
print("split",a.split(","))



# String Concatenation
a = "Hello"
b = "World"
c = a + b
print("string Concatenation :-",c)

c = a + " " + b
print(c)