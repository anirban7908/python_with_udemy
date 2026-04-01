# from turtle import *
# timmy = Turtle()

# print(timmy)

# timmy.shape('turtle')
# timmy.color("red")

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# my_screen = Screen()
# my_screen.exitonclick()
# # print(my_screen.canvheight)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",
["Bulbasaur","Charmander","Pikachu","Gyarados","Squirtle"])
table.add_column("Type",
["Grass, Poison","Fire","Electric","Water, Flying","Water"])
table.align = "l"
print(table)