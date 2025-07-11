#!/bin/env python
from pprint import pprint
import argparse
import json
import os


def main():
    descr = "Prints out a easy to read version of SDR++ JSON export"
    parser = argparse.ArgumentParser(
        prog='display',
        description=descr,
    )
    parser.add_argument('filename')

    args = parser.parse_args()
    filename = str(args.filename)

    # Checking if file exsists
    if not os.path.exists(filename):
        print("File not found")
        return 0

    # Loading data
    with open(filename, 'r') as file:
        json_data = json.load(file)

    bookmarks = json_data.get('bookmarks')
    freq_data = {}
    max_item_len = 0
    item_len = []
    for data in bookmarks:
        frequency = bookmarks.get(data).get('frequency')
        if frequency:
            frequency = int(frequency) / (10**6)
            item_len.append(len(str(frequency)))
            freq_data[data] = frequency

    # Print the data with aligned columns
    max_item_len = max(item_len)
    max_key_len = max(len(key) for key in freq_data)

    for key, value in freq_data.items():
        print(f"{key:<{max_key_len}}: {value:<{max_item_len}} MHz")


if __name__ == "__main__":
    main()
