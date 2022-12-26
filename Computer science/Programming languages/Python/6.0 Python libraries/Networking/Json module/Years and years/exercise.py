# Years and years
# Convert the dictionary below to a JSON string named 
# years_json. Specify the indent as 4.

import json


years = {2020: "leap year", 2021: "regular year", 2022: "regular year",
         2023: "regular year", 2024: "leap year"}

# convert years to JSON string
years_json = json.dumps(years, indent=4)