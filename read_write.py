"""
A script to demonstrate reading and writing
different file types in Python.
"""

# empty list to store file lines
text_contents = []

# open the file. f is a variable that stores the
# connection to the file while it is open
with open('data/example.txt', 'r') as f:
    text_contents = f.readlines()

# after the with statement, the file is closed 
# and the connection (f) is deleted.
print(text_contents)

# The \n character in the output is a special character
# for a newline