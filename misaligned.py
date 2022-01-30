def print_color_map(major_color, minor_color, pair_number):
    print(f'{pair_number} | {major_color} | {minor_color}')


def create_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []

    for i, major_color in enumerate(major_colors):
        for j, minor_color in enumerate(minor_colors):
            print_color_map(major_color, minor_color, (i * 5 + j)+1)
            color_map.append(f'{(i * 5 + j)+1} | {major_color} | {minor_color}')

    return len(major_colors) * len(minor_colors), color_map


result, color_map = create_color_map()

assert (color_map[0] == '1 | White | Blue')
assert (color_map[2] == '3 | White | Green')
assert (color_map[15] == '16 | Yellow | Blue')
assert (color_map[24] == '25 | Violet | Slate')
print("All is well (maybe!)\n")
