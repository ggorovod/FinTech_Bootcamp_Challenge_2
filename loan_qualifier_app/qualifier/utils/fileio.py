# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

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

#def save_csv_data(csvpath, data, header=None):
def save_csv_data(qualified_loans_csv):
    
    """csvpath here is the outpaht"""
    
    
    
    output_path = Path("qualifying_loans.csv")
    csvpath = output_path       
       
       
    header = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter =',')
        csvwriter.writerow(header)
        for bank in qualified_loans_csv:
            csvwriter.writerow(bank)
    return qualified_loans_csv
            
            
    """with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        if header:
            csvwriter.writerow(header)
        #for data in qualified_loans_csv
        csvwriter.writerows(data)"""

