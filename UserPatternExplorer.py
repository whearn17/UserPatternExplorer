import argparse
import csv
from collections import defaultdict
import os


def analyze_logs(logfile, user_column, columns, outfile):
    user_data = defaultdict(lambda: defaultdict(set))

    with open(logfile, 'r', newline='') as f:
        reader = csv.DictReader(f, delimiter=',')  # assumes comma-separated values
        for row in reader:
            user = row[user_column]
            for column in columns:
                user_data[user][column].add(row[column])

    with open(outfile, 'w', newline='') as f:  # add newline='' to prevent additional newlines
        writer = csv.writer(f)

        # prepare the header
        header = ['User']
        for column in columns:
            header.append(column + ' Count')
            header.append(column + ' List')
        writer.writerow(header)

        # write the data
        for user, data in user_data.items():
            row = [user]
            for column in columns:
                unique_items = data[column]
                row.append(len(unique_items))
                row.append(", ".join(unique_items))
            writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(description='Analyze user behavior in logs.')
    parser.add_argument('-f', required=True, help='Input CSV file')
    parser.add_argument('-u', required=True, help='Name of the user column')
    parser.add_argument('-c', required=True, help='Names of the cells to analyze, separated by colon')

    args = parser.parse_args()

    logfile = args.f
    outfile = os.path.splitext(logfile)[0] + '_behavior_analysis.csv'  # add the suffix before the file extension
    user_column = args.u
    columns = [col.strip() for col in
               args.c.split(':')]  # split the string into a list of column names, remove extra spaces

    analyze_logs(logfile, user_column, columns, outfile)


if __name__ == "__main__":
    main()
