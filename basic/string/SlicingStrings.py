# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:6])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
print("Slice From the Start",b[:5])


# Slice To the End
print("Slice To the End",b[2:])