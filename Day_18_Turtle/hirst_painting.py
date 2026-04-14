import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 50)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
def get_rgb(colors):
    final_colors = []
    for color in colors:
        rgb = color.rgb # e.g. (255, 151, 210)
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        color_rgb = (r,g,b)
        final_colors.append(color_rgb)
    return final_colors

print(len(get_rgb(colors)))