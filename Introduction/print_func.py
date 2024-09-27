# The print function is used to output text or other data to console. 
# # Syntax - print(*objects, sep=' ', end='\n', file=sys.stdout, flush = False)
# *objects - Any number of objects to be printed.
# sep - define how to separate, by default " "
# end -  define what print at the end , by default newline
# file - the file in which output should written, by default sys.stdout
# flush - defines whether to forcibly flush the stream, by default False

print("hello", "World",sep="-",end="~!")

# Printing to a file
with open("text.txt","w") as file:
    print("New Creation", file=file)

# Formatting Strings
name = "Annant"
age = 32
print(f"Name: {name},Age: {age}")

