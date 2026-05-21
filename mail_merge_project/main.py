#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Paths 
NAMES = "Input/Names/invited_names.txt"
LETTERS = "Input/Letters/starting_letter.txt"
READY_LETTERS = "Output/ReadyToSend"

name_list = []
letter_body = None
with open(NAMES, "r") as names:
    name_list = names.readlines()

with open(LETTERS, "r") as letter:
    actual_letter_body = letter.read()
    for name in name_list:
        clean_name = name.strip()
        current_letter_body = actual_letter_body.replace("[name]",clean_name)
        with open(f"{READY_LETTERS}/{clean_name}.txt", "w") as ready_letter:
            ready_letter.write(current_letter_body)
    
