# import csv
# with open("weather_data.csv") as csvfile:
#     data=csv.reader(csvfile)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas
from numpy.ma.extras import average

data = pandas.read_csv("weather_data.csv")
list_temp=data["temp"].tolist()
#sum=0
# for item in list_temp:
#     sum+=int(item)
# print(sum/len(list_temp))

# average = average(list_temp)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())

#getting the row that has the highest temperature
# print(data[data.temp==data["temp"].max()])

# monday = data[data.day=="Monday"]
# print(monday.temp)
# converted_temp=(monday.temp * 1.8)+32
# print(converted_temp)

##creating the dataframe from dict
data_dict={
    "students":["amy","james","arsh"],
    "scores":[76,56,65]
}

data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("student_data.csv")
