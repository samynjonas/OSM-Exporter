# Automatically extract OSM data using python
import requests

print("Started exporting OSM data...")

# Output file path
output_file = "osm_data.json"

# Box coordinates
coordinates = [30.618338, -96.323712, 30.625000, -96.316000]

# All data you want to check for and save
dataToExport = [ 
    """way["highway"="primary"]""",
    """way["highway"="secondary"]""",
    """way["highway"="tertiary"]""",
    """way["highway"="residential"]""",
    """way["railway"="tram"]"""
    ]


# Define the API endpoint
overpass_url = "http://overpass-api.de/api/interpreter"

# Define the Overpass QL querry
overpass_query = f"""
[out:json]
[timeout:90];
(
"""
for line in dataToExport:
    overpass_query += f"    {line}(\n{coordinates[0]},\n{coordinates[1]},\n{coordinates[2]},\n{coordinates[3]}\n);\n"
overpass_query += """
);
out body;
>;
out skel qt;
"""

# Make the request
response = requests.get(overpass_url, params={'data': overpass_query})
if response.status_code == 200:
    # Write the response to the output file
    with open(output_file, 'w') as f:
        f.write(response.text)
    print(f"Data written to {output_file}")
else:
    print(f"Error: Failed to retrieve data. Status code: {response.status_code}")

data = response.json()

# Print the data to check
# print(data)
print("Done processing data!!")
