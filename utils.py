
import json
import csv


def json_to_csv(json_file, csv_file):
  with open(json_file) as f:
    jsondata = json.load(f)

  data_file = open(csv_file, 'w', newline='')
  csv_writer = csv.writer(data_file)

  count = 0
  for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

  data_file.close()