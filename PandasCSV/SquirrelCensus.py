import pandas
PATH = "/home/manu/100-Days-of-Code/PandasCSV/"

data = pandas.read_csv(PATH + "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"]
print(colors)

gray = 0
cinnamon = 0
black = 0
other_color = 0

for color in colors:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1
    else:
        other_color += 1

# print(gray)
# print(cinnamon)
# print(black)
# print(other_color)

color_dict = {'Color': ['Gray', 'Cinnamon', 'Black', 'Other Color'],
		'Count': [gray, cinnamon, black, other_color]
}


format_dict = pandas.DataFrame(color_dict)

format_dict.to_csv(PATH + "FormatColors.csv")