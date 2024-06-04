
# * FILENOTFOUND 
try:
    with open("a_file.txt") as file:
        file.read()
except FileNotFoundError:
    print("ERROR!")
except KeyError as error_message:
    print(f"That key don't exist!, error -> {error_message}")
else:
    print("No errors!")
finally:
    print("Error management errors ended!")


a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]


fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

text = "abc"
print(text + 5)


# * Handling Exceptions KEYWORDS

# * try:

# * except:

# * else:

# * finally:



# * raise:
# * This keyword help us to raise our on exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")



bmi = weight / height ** 2

print(bmi)