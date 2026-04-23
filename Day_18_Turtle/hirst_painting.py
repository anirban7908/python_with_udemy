import colorgram
import turtle as t
import random
# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 50)

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# def get_rgb(colors):
#     final_colors = []
#     for color in colors:
#         rgb = color.rgb # e.g. (255, 151, 210)
#         r = rgb[0]
#         g = rgb[1]
#         b = rgb[2]
#         color_rgb = (r,g,b)
#         final_colors.append(color_rgb)
#     return final_colors

# print(len(get_rgb(colors)))

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)


color_list = [(226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215), (244, 227, 95), (173, 20, 41), (233, 79, 51), (224, 126, 156), (118, 184, 130), (11, 172, 207), (165, 151, 25), (13, 58, 148), (83, 37, 23), (128, 37, 27), (37, 129, 78), (42, 192, 160), (14, 39, 92), (129, 238, 190), (244, 162, 151), (235, 162, 181), (100, 101, 186), (127, 214, 239), (66, 77, 38), (74, 31, 46), (20, 93, 54), (160, 175, 234), (254, 238, 0), (26, 65, 48), (251, 7, 38)]

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


scr = t.Screen()
scr.exitonclick() 