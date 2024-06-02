import pandas as pd
PATH = "/home/manu/100-Days-of-Code/DoneExersices/NATOalphabet/"
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:
# * {"A": "Alfa", "B": "Bravo"}
with open(PATH + "/nato_phonetic_alphabet.csv") as alphabet:
    pd_alphabet_format = pd.read_csv(alphabet)
    pd_alphabet_dict = pd_alphabet_format.to_dict()

format_list_letter = pd_alphabet_dict.get("letter")
format_list_code = pd_alphabet_dict.get("code")
dictionary = {}
for code in format_list_letter:
    dictionary[format_list_letter[code]] = format_list_code[code]


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_in = input("What is the word you wanna spell in NATO alphabet?\n-> ")


user_in_format = [n for n in user_in.upper()]

transformed_user_in = [dictionary[letter] for letter in user_in_format]

print(transformed_user_in)

