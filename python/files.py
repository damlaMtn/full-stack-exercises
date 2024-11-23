## READ ##

# Open the file in read ('r') mode
file = open('file.txt', 'r')

#---------------------------------

# Reading and Storing the Entire Content of a File

# Using the read method, you can retrieve the complete content of a file
# and store it as a string in a variable for further processing or display.

# Step 1: Open the file you want to read
with open('file.txt', 'r') as file:

    # Step 2: Use the read method to read the entire content of the file
    file_stuff = file.read()

    # Step 3: Now that the file content is stored in the variable 'file_stuff',
    # you can manipulate or display it as needed.

    # For example, let's print the content to the console:
    print(file_stuff)

# Step 4: The 'with' statement automatically closes the file when it's done,
# ensuring proper resource management and preventing resource leaks.

#---------------------------------

file = open('file.txt', 'r')
line1 = file.readline()  # Reads the first line
line2 = file.readline()  # Reads the second line
print(line1)  # Print the first line
if 'important' in line2:
    print('This line is important!')

while True:
    line = file.readline()
    if not line:
        break  # Stop when there are no more lines to read
    print(line)
file.close()

#------------------------------------

file = open('file.txt', 'r')
file.seek(10)  # Move to the 11th byte (0-based index)
characters = file.read(5)  # Read the next 5 characters
print(characters)
file.close()

#-----------------------------------------------------------------------------

## WRITE ##

# Create a new file Example2.txt for writing
with open('Example2.txt', 'w') as file1:
    file1.write("This is line A\n")
    file1.write("This is line B\n")
    # file1 is automatically closed when the 'with' block exits

#--------------------------------------

# List of lines to write to the file
Lines = ["This is line 1", "This is line 2", "This is line 3"]

# Create a new file Example3.txt for writing
with open('Example3.txt', 'w') as file2:
    for line in Lines:
        file2.write(line + "\n")
    # file2 is automatically closed when the 'with' block exits

#--------------------------------------

# Data to append to the existing file
new_data = "This is line C"

# Open an existing file Example2.txt for appending
with open('Example2.txt', 'a') as file1:
    file1.write(new_data + "\n")
    # file1 is automatically closed when the 'with' block exits

#--------------------------------------

# Open the source file for reading
with open('source.txt', 'r') as source_file:
    # Open the destination file for writing
    with open('destination.txt', 'w') as destination_file:
        # Read lines from the source file and copy them to the destination file
        for line in source_file:
            destination_file.write(line)
    # Destination file is automatically closed when the 'with' block exits
# Source file is automatically closed when the 'with' block exits

#--------------------------------------

