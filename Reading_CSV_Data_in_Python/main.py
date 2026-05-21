import csv

# with open("weather_data.csv", mode="r") as data:
#     print(data.readlines())


# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
        
#     print(temps)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(temps[0])
# print(type(temps))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
temp_mean = data['temp'].mean()
max_temp = data['temp'].max()

# avg_temps = sum(temp_list)/len(temp_list)
# print(temp_list)
# print(sum(temp_list))
# print(len(temp_list))
# print(avg_temps)

# print(max_temp)

# get the data in row
# print(data[data.day == "Monday"])


# get the row with highest temperature
# print(data[data.temp == data.temp.max()])


# get the max temperatue in fahrenheit
max_temp_in_celcius = data.temp.max()
max_temp_in_fahrenheit = (max_temp_in_celcius * 1.8) + 32
print(f"The max temp in fahrenheit is: {max_temp_in_fahrenheit}")


# Get a perticular day temperature in fahrenheit
monday = data[data.day == "Monday"]
monday_temp_in_celcius = monday.temp[0]
monday_temp_in_fahrenheit = (monday_temp_in_celcius * 1.8) + 32
print(f"The temp pf monday in fahrenheit is: {monday_temp_in_fahrenheit}")


# Create dataframe for scratch
data_dict = {
    "Student" : ["John", "Jenny", "Jonnah"],
    "Score":[20,30,40]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")