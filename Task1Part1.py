# Part 1: Extracting and Storing Fields in restaurants.csv file
import requests, json, csv, os, openpyxl

# Get country codes and respective countries from xlsx file
workbook = openpyxl.load_workbook('Country-Code.xlsx')
sheet = workbook.active
country_ids = {}

for row in sheet.iter_rows(values_only=True):
    country_ids[row[0]] = row[1]
del country_ids['Country Code'] # Remove headers row
workbook.close()

# Read restaurant information from json file via url
url = 'https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json'
data = json.loads(requests.get(url).text)

# Create list of all restaurants
restaurants = []
for row in data:
    for restaurant in row['restaurants']:
        restaurants.append(restaurant)

# (During Testing) Ensure existing file contents are removed first
filePath = 'restaurants.csv'
if os.path.exists(filePath):
    os.remove(filePath)

# Write data to restaurants.csv
with open('restaurants.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Restaurant Id', 'Restaurant Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines'])
        writer.writeheader()

        # Get required information for each restaurant
        for restaurant in restaurants:
            id = restaurant['restaurant']['R']['res_id']
            name = restaurant['restaurant']['name']
            country = restaurant['restaurant']['location']['country_id']
            city = restaurant['restaurant']['location']['city']
            urv = restaurant['restaurant']['user_rating']['votes']
            uar = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
            cuisines = restaurant['restaurant']['cuisines']

            # If country is a valid country, write to file
            if int(country) in country_ids:
                writer.writerow({'Restaurant Id': id, 'Restaurant Name': name, 'Country': country_ids[int(country)], 'City': city, 'User Rating Votes':urv, 'User Aggregate Rating': uar, 'Cuisines': cuisines})

csvfile.close()

if __name__ == 'main':
    if os.path.isfile('restaurants.csv'):
        print("Task 1 Part 1 Completed.\n restaurants.csv file has been generated.")
    else:
        print("Error.")