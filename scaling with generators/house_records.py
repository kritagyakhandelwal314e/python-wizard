from pprint import pprint
def house_records(path):
  with open(path) as lines:
    records = {}
    for line in lines:
      if line == '\n':
        yield records
        records = {}
      else:
        key, value = line.rstrip('\n').split(': ', 1)
        records[key] = value
  yield record

for record in house_records('house_records.txt'):
  pprint(record)