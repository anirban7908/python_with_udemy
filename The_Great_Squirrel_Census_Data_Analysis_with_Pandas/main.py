import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data_20260521_2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260521.csv")

grey_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Black"])

squirrel_data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrel_data_dict)

df.to_csv("squirrel_count.csv")