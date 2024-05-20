from os import name
from art import logo 
from art import vs
from data import data
import random


print(logo)


print(vs)


first_option = random.choice(data)


name = first_option["name"]
followers = first_option["follower_count"]
description = first_option["description"]
country = first_option["country"]
first_person_data = [name, followers, description, country]

print(f"{first_person_data[0]} is a {first_person_data[2]} from {first_person_data[3]}, it has {first_person_data[1]} millions of followers")

second_option = random.choice(data)

while second_option == first_option:
    second_option = random.choice(data)

print(second_option)


def data_extract():
