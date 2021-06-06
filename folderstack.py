import os
import click

dir = "/Users/hamishgibbs/Documents/Covid-19/fb_population_paper/src/"

folder_end = "└── "
folder = "├── "


@click.command()
@click.option('--dir', default=os.getcwd(), help='root directory to document')
@click.option('--outfile',
              default=os.getcwd() + "/folderstack.md",
              help='output Markdown file')
@click.option('--docspace',
              default=50,
              help='space before documentation')
def cli(dir, outfile, docspace):

    out_lines = document_directory(dir, docspace)

    with open(outfile, "w") as f:

        f.writelines("\n".join(out_lines))


def format_file(name, last_items, recursion_level, directory=False):

    if name in last_items:

        folder_symbol = folder_end

    else:

        folder_symbol = folder

    if directory:
        recursion_level = recursion_level

    space = "  " * recursion_level
    return space + folder_symbol + name


def document_directory(dir, docspace):

    original_root_len = len(dir.split(os.sep)) - 1

    last_items = []
    out_lines = []

    for root, dirs, files in os.walk(dir):
        path = root.split(os.sep)

        recursion_level = len(path) - original_root_len - 1

        if len(dirs) != 0:
            last_items.append(dirs[-1])
        elif len(files) != 0:
            last_items.append(files[-1])
        else:
            continue

        out_lines.append(
            format_file(
                name=os.path.basename(root),
                last_items=last_items,
                recursion_level=recursion_level,
                directory=True))

        for i, file in enumerate(files):
            out_lines.append(
                format_file(
                    name=file,
                    last_items=last_items,
                    recursion_level=recursion_level,
                    directory=False))

    out_lines = [x + " " * (docspace - len(x)) + "#" for x in out_lines]

    out_lines = ["```"] + out_lines + ["```"]

    return out_lines
