import Task1Part1
import json

threshold = {'Excellent': -1.0,
          'Very Good': -1.0,
          'Good': -1.0,
          'Average': -1.0,
          'Poor': -1.0,
          }

for restaurant in Task1Part1.restaurants:
    res_grade_text = restaurant['restaurant']['user_rating']['rating_text']
    res_grade = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
    if res_grade_text in threshold:
        if threshold[res_grade_text] == -1.0:
            threshold[res_grade_text] = res_grade
        elif res_grade < threshold[res_grade_text]:
            threshold[res_grade_text] = res_grade

print(json.dumps(threshold))
