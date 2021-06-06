import os

dir = "/Users/hamishgibbs/Documents/Covid-19/fb_population_paper/src/"

folder_end = "└── "
folder = "├── "


def format_file(name, last_items, recurstion_level, space = 3):

    if name in last_items:

        folder_symbol = folder_end

    else:

        folder_symbol = folder

    space = " " * space
    return recursion_level * space + folder_symbol + name


original_root_len = len(dir.split(os.sep)) - 1

last_root = ""
last_items = []
out_lines = []

for root, dirs, files in os.walk(dir):
    path = root.split(os.sep)
    if len(dirs) == 0:
        last_items.append(files[-1])
    else:
        last_items.append(dirs[-1])

    recursion_level = len(path) - original_root_len

    out_lines.append(format_file(os.path.basename(root), last_items, recursion_level, space = 3))

    for i, file in enumerate(files):
        out_lines.append(format_file(file, last_items, recursion_level, space = 6))

out_lines = [x + " " * (50 - len(x))  + "#" for x in out_lines]

out_lines = ["```"] + out_lines + ["```"]

out_lines
