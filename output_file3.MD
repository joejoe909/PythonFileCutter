In this code, we first open the file 'filename.txt' for reading using the open() function. We then use the read() method of the file object to read the entire contents of the file into a variable called file_contents. Finally, we print the contents of the file using the print() function. You can replace 'filename.txt' with the actual filename of the text file you want to read.

'''
# Open the file for reading
with open('input.txt', 'r') as file:

    # Read the contents of the file into a variable
    file_contents = file.read()

# Print the contents of the file
print(file_contents)
'''
[/Text]
