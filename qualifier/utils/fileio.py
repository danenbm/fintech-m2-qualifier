# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains helper functions for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from the path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, header, data):
    """Saves the CSV file to the path provided.

    Args:
        csvpath (Path): The CSV file path.
        header (list): The CSV header.
        data (list of lists): A list of lists that contains the rows
                              of data from the CSV file.
    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")

        # Write the header.
        csvwriter.writerow(header)

        # Write each row of data to the csv file.
        for row in data:
            csvwriter.writerow(row)
