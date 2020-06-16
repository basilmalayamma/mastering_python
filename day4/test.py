import json

def write_to_file(name, data):
    handle = open(name, "w")
    handle.write(data)
    handle.close

def read_file(name):
    handle = open(name)
    data = handle.read()
    handle.close()
    return data

my_dict ={
    'limbo': {
        'artist': 'Daddy Yankee',
        'album': 'prestige',
        'year': 2012
        },
    'travesuras': {
        'artist': 'Nicky Jam',
        'album': 'travesuras',
        'year': 2014
        },
    'duele el corazon': {
        'artist': ['Enrique Iglesias', 'Wisin'],
        'album': 'duele el corazon',
        'year': 2016
        }
    }

json_data = json.dumps(my_dict)
#print(json_data)
write_to_file("json.txt",json_data)
data = read_file("json.txt")
json_data1 = json.loads(data)
print(json_data1)
print("$"*60)
print(json_data1['duele el corazon'])
print("$"*60)
try:
    print(json_data1['Basi'])
except KeyError:
    print("Not found")
