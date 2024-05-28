#TODO: Create a letter using starting_letter.txt 


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        


# Formated Names in list
names_format = []


with open("/home/manu/100-Days-of-Code/MailMergeProject/Input/Names/invited_names.txt") as names:
    str_names = names.read()
    name_list = str_names.split()
    for name in name_list:
        names_format.append(name)
        
        
with open("/home/manu/100-Days-of-Code/MailMergeProject/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names_format:
         with open(f"/home/manu/100-Days-of-Code/MailMergeProject/Output/ReadyToSend/LetterTo{name}.txt", "w") as finalletter:
                finalletter.write(letter_content.replace("[name]", name))
            
    




