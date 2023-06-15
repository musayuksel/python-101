from colorama import init, Fore, Style
import os

init()  # initialize Colorama


def print_tree(path, prefix="", level=0):
    colors = [
        Fore.WHITE,
        Fore.BLUE,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.MAGENTA,
    ]

    color = colors[level % len(colors)]
    for item in os.scandir(path):
        print(color + prefix + "├── " + item.name)
        if item.is_dir():
            print_tree(item.path, prefix + "│   ", level + 1)
    print(Style.RESET_ALL, end="")


print_tree("/Users/musayuksel/Documents/GitHub/python-101/LinkedIn")
