import pandas as pd
PATH = "/home/manu/100-Days-of-Code/DoneExersices/NATOalphabet/"


with open(PATH + "/nato_phonetic_alphabet.csv") as alphabet:
    pd_alphabet_format = pd.read_csv(alphabet)
    pd_alphabet_dict = pd_alphabet_format.to_dict()

format_list_letter = pd_alphabet_dict.get("letter")
format_list_code = pd_alphabet_dict.get("code")
dictionary = {}
for code in format_list_letter:
    dictionary[format_list_letter[code]] = format_list_code[code]

is_on = True
while is_on:
    user_in = input("What is the word you wanna spell in NATO alphabet?\n-> ")
    try:
        user_in_format = [n for n in user_in.upper()]
        transformed_user_in = [dictionary[letter] for letter in user_in_format]
        print(transformed_user_in)
        is_on = False
    except:
        print("This program only handle alphabet characters!\n")
