import json
from datetime import datetime

# create a dictionary to be saved as JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

file_name = f"test_{now.strftime('%Y%m%d%H%M%S')}.json"

print(f"Creating the file {file_name}...")

# write the dictionary to a JSON file
with open(file_name, "w") as outfile:
    json.dump(data, outfile)

print(f"The {file_name} file was generated.")
