# # with open("weather_data.csv") as file:
# #     week_forcast = [line.rstrip("\n") for line in file]

# # print(week_forcast)

# # import csv

# # with open("weather_data.csv") as file:
# #     week_forcast = csv.reader(file)
# #     temperature  = []
# #     for row in week_forcast:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))

# #     print(temperature)


# import pandas

# weather = pandas.read_csv("weather_data.csv")
# # print(type(weather))
# # print(weather["temp"])    


# # weather_dict = weather.to_dict()
# # print(weather_dict)

# temp_list = weather["temp"].to_list()
# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
# avg_temp = total_temp / len(temp_list)
# # print(f"{avg_temp :.2f}")

# # print(weather["temp"].mean())

# # print(weather["temp"].max())

# # #Get data from column
# # print(weather.condition)

# #Get data from row
# # print(weather[weather.day == "Monday"])
# # print(weather[weather.temp == weather.temp.max()])

# mon_temp = weather.temp[weather.day == "Monday"]
# farenht = mon_temp * 9/5 + 32

# print(farenht)

import pandas
# Create data-frame from scratch 

data_dict = {
    "students": ["Amy", "Gerald", "Jason"],
    "scores": [70, 58, 81]
}

data = pandas.DataFrame(data_dict)

print(data)
data.to_csv("new_file.csv")