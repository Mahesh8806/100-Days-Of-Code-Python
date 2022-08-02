#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    # print(name)



with open("./Input/Letters/starting_letter.txt",mode='r') as letter_file:
    letter_content = letter_file.read()
    print(letter_content)
    for name in names:
        striped_name = name.strip()
        content = letter_content.replace(PLACEHOLDER, striped_name)
        print(content)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.docx",mode='w') as completed_letter:
            completed_letter.write(content)


