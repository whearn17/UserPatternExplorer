# UserPatternExplorer
 
UserPatternExplorer is a Python-based tool designed to analyze user behavior in logs. It navigates through CSV log files to track and record unique user activities based on specified data fields (e.g., Country, Region, ISP). The output provides an insightful view of the diverse behaviors exhibited by users, thereby aiding in activities such as anomaly detection, user behavior profiling, and more.

## Features

* Takes input CSV log file and user-defined column names dynamically.
* Tracks unique items per user per specified column.
* Outputs a detailed CSV file with counts and lists of unique values for each user and column.

## Requirements
Python 3.6+

## Usage
UserPatternExplorer can be run from the command line with the following arguments:

```
python UserPatternExplorer.py -f input.csv -u UserColumnName -c Column1Name:Column2Name:Column3Name:etc
```

* -f: Path to the input CSV file
* -u: Name of the user column in the CSV file
* -c: Names of the cells to analyze, separated by colon (:)

The output CSV file will be named using the input file's name appended with '_behavior_analysis.csv'.

## Example
Given an input CSV file login_data.csv with a 'User' column and 'Country', 'Region', 'ISP' columns, you would run:

```
python UserPatternExplorer.py -f login_data.csv -u User -c Country:Region:ISP
```

This would create an output file login_data_behavior_analysis.csv with the 'User' column followed by pairs of 'Count' and 'List' columns for each specified cell.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
William Hearn | Surefire Cyber Inc.
