# String literals are sequences of characters used to represent text in programming. They are typically enclosed in quotation marks.

# 1. Single-Quoted Strings: Enclosed in single quotes (').
'Hello, World!'

# 2. Double-Quoted Strings: Enclosed in double quotes (").
"Hello, World!"

# 3. Triple-Quoted Strings: Enclosed in triple quotes (''' or """). These can span multiple lines.
"""This is a
multi-line string"""

# Escape Sequences 
# Escape sequences are used to include special characters in string literals:

# \n : Newline
# \t : Tab
# \\ : Backslash
# \' : Single quote
# \" : Double quote

# Raw Strings
# Raw strings treat backslashes as literal characters and are useful for regular expressions and file paths.
r"C:\Users\Name"  # Output: C:\Users\Name

# String Interpolation
# Many languages support string interpolation, allowing variables to be embedded directly within string literals:
name = "Alice"
greeting = f"Hello, {name}!"
