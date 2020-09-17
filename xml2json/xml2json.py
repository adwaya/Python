import json
import xmltodict

# Open the file
with open("feed.xml") as xml_file:

	data_dict = xmltodict.parse(xml_file.read())
	xml_file.close()
    # Convert to a json object
	json_data = json.dumps(data_dict)

	# Write the json data to output
	# json file
	with open("data.json", "w") as json_file:
		json_file.write(json_data)
		json_file.close()
