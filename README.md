# GDS_CC4
CC4 Internship 2024 Div Tech Assessment

## Requirements
- Python 3
- Libraries: requests, json, csv, os, openpyxl, datetime

## Instructions 
- Download "Task1Part1.py", "Task1Part2.py", "Task1Part3.py" and "Country-Code.xlsx" and save into a folder.
- Navigate to the folder in command prompt/terminal with 'cd ../folder_name'
- Run each task with 'python Task1Part1.py', 'python Task1Part2.py' or 'python Task1Part3.py' respectively. Note that Task1Part1 should be run first before the other two tasks.
- 'Task 1 Part X completed.' will be returned upon successfully running the code.

## Task 1: Part 1
This task requires the file "Country-Code.xlsx". It returns a "restaurants.csv" file.
### Assumptions/Interpretations:
- Entries with invalid country ID can be ignored because the localities are noted as "Dummy", which implies a dummy entry.

## Task 1: Part 2
This task requires the file for the first task, 'Task1Part1.py'. It returns a "restaurant_events.csv" file that contains the information of all events that happened in April 2019.
### Assumptions/Interpretations: 
- Any event with start date in April 2019 will be added, regardless of end date.

## Task 1: Part 3
This task requires the file for the first taks, 'Task1Part1.py'. It returns the threshold of each text grade.
### Assumptions/Interpretations:
- Threshold is defined as the minimum aggregate rating a restaurant must get for each text grade.
- Assume that the dataset contains at least one restaurant that hits threshold value for each text grade.
