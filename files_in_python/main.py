# # Open a file
# file = open("my_text.txt")

# # Read a file
# content = file.read()

# # Print file content
# print(content)

# # close the file
# file.close()


# Open a file by with. Her we don't need to close the file "with" will close the file automatically
with open("my_text.txt") as file:

    # Read a file
    content = file.read()

    # Print file content
    print(content)
    
# Write something inside a file. We can use multiple modes inside "with" like "a" = append/add new content, "w" = will overwrite the new content with the existing data, and the defalut is r = read only mode
with open("my_text.txt", mode="a") as file:
    file.write("\nThis is new line")

with open("my_text.txt") as file:

    # Read a file
    new_content = file.read()

    # Print file content
    print(new_content)