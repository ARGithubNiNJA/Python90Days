import pandas

data=pandas.read_csv('Squirrel.csv')
gray_squirrals_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrals_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrals_count=len(data[data["Primary Fur Color"]=="Black"])

# print(gray_squirrals_count)
# print(red_squirrals_count)
# print(black_squirrals_count)

data_dict={
   "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrals_count,red_squirrals_count,black_squirrals_count]
}

print(data_dict)
tab_data=pandas.DataFrame(data_dict)
print(tab_data)
tab_data.to_csv('Squirrel_Fur_wise_count.csv')