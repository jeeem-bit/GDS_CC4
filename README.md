# GDS_CC4
CC4 Internship 2024 Div Tech Assessment

## Requirements
- Python 3
- Libraries: requests, json, csv, os, openpyxl, datetime

## Task 1: Part 1
This task requires the file "Country-Code.xlsx". It returns a "restaurants.csv" file.
### Assumptions/Interpretations:
- Entries with invalid country ID can be ignored because the localities are noted as "Dummy", which implies a dummy entry.

## Task 1: Part 2
This task requires the file for the first task, 'Task1Part1.py'. It returns a "restaurant_events.csv" file that contains the information of all events that happened in April 2019.
### Assumptions/Interpretations: 
- Any event with start date in April 2019 will be added, regardless of end date.

## Task 1: Part 3
This task requires the file for the first taks, 'Task1Part1.py'. It returns a dictionary showing the threshold of each text grade.
### Assumptions/Interpretations:
- Threshold is defined as the minimum aggregate rating a restaurant must get for each text grade.
- Assume that the dataset contains at least one restaurant hititng threshold value for each text grade.
