import pandas
PATH = "/home/manu/100-Days-of-Code/PandasCSV/"

data = pandas.read_csv(PATH + "weather_data.csv")
# print(type(data))
# print(type(data))


# data_dict = data.to_dict()

# print(data_dict)


temp_list = data["temp"].to_list()
print(len(temp_list))
print(temp_list)

sum_list = sum(temp_list)

avg_temp = sum_list / len(temp_list)

print(avg_temp)

# * Data in columns 

print(data["condition"])
print(data.condition)


# * Data in rows 

print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)
mon_temp_f = (monday.temp * 9/5) + 32
print(f"{mon_temp_f}") 