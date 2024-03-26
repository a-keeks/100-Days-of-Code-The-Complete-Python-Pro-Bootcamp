import pandas

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_squirrel_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
gray_squirrel_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])



squirrel_fur_dict = {
    "Fur Colour": ["Black", "Gray", "Cinnamon"],
    "Count": [black_squirrel_count, gray_squirrel_count, cinnamon_squirrel_count]
}

squirrel_fur_dataframe = pandas.DataFrame(squirrel_fur_dict)

squirrel_fur_dataframe.to_csv("squirrel_count.csv")