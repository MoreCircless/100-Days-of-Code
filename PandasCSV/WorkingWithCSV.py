# with open("/home/manu/100-Days-of-Code/PandasCSV/weather_data.csv") as file_data:
#     data = file_data.readlines()

# print(data)


# import csv

# with open("/home/manu/100-Days-of-Code/PandasCSV/weather_data.csv") as file_data:
#     data = csv.reader(file_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))    
#     print(temperatures)
        
        
import pandas

data = pandas.read_csv("/home/manu/100-Days-of-Code/PandasCSV/weather_data.csv")
print(data["temp"])



