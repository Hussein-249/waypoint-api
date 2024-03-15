import os
import csv
# import pandas as pd


def read_csv(filename: str) -> None:
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            # Remove trailing comma and newline
            if line.endswith(",\n"):
                line = line[:-2] + "\n"
            f.write(line)
    """Reads a csv file, returns none"""

    # with open ensures file will be closed even when exception

    # count = 0
    # with open(filename, newline='') as csv_file:
    #     reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    #     for row in reader:
    #         print(','.join(row))
    #
    #         count += 1
    # print(count)
    return None


def menu():
    print(f"Select a menu option:")
    print(f" 1 view files in current directory | 2 Read a csv file")
    print_working_dir()

    read_csv("../resources/CANADA_WAYPTS.csv")
    return 0


def print_working_dir():
    dir_files = os.listdir()

    print(f"WORKING DIRECTORY:")
    for file in dir_files:
        if os.path.isfile(file):
            print(file)


if __name__ == '__main__':
    menu()
