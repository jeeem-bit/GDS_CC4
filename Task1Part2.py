# Part 2: Extracting restauarants that have past event in month of April 2019
import requests, json, csv, os
from datetime import datetime   
import Task1Part1

# Read data
url = 'https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json'
data = json.loads(requests.get(url).text)

# (During Testing) Ensure existing file contents are removed first
filePath = 'restaurant_events.csv'
if os.path.exists(filePath):
    os.remove(filePath)

# Write data to restaurant_events.csv
with open('restaurant_events.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Event Id', 'Restaurant Id', 
                                                     'Restaurant Name', 'Photo URL', 
                                                     'Event Title', 'Event Start Date', 
                                                     'Event End Date'])
        writer.writeheader()

        for restaurant in Task1Part1.restaurants:
        # If the restaurants have events, start check
            if 'zomato_events' in restaurant['restaurant']:
                for event in restaurant['restaurant']['zomato_events']:
                    event_start_date = event['event']['start_date']
                    date = datetime.strptime(event_start_date, '%Y-%m-%d')
                    # If event starts in April 2019, write to file
                    if date.month == 4 and date.year == 2019:
                        id = event['event']['event_id']
                        res_id = restaurant['restaurant']['R']['res_id']
                        res_name = restaurant['restaurant']['name']
                        event_photos_url = event['event']['photos']
                        event_photo_urls = [photo['photo']['url'] for photo in event_photos_url] # Create an array for all photo urls
                        title = event['event']['title']
                        start = event['event']['start_date']
                        end = event['event']['end_date']
                        writer.writerow({'Event Id': id, 'Restaurant Id': res_id, 
                                         'Restaurant Name': res_name, 'Photo URL': "NA" if not event_photo_urls else event_photo_urls, 
                                         'Event Title':title, 'Event Start Date': start, 
                                         'Event End Date': end})
                        
csvfile.close()
