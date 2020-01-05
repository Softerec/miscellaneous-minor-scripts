# -*- coding: utf-8 -*-
"""
Script shows how to pack & unpack numpy dictionary (into json file).
Checks also if content before and after is equal.
"""
import io
import jsonpickle

# jsonpickle includes a built-in numpy extension,
# to encode sklearn models, numpy arrays, and other numpy-based data 
# then you must enable the numpy extension by registering its handlers: 
import jsonpickle.ext.numpy as jsonpickle_numpy
jsonpickle_numpy.register_handlers()

# import of numpy to be able to pack and unpack numpy format data
import numpy as np

# numpy example of data to present packing and unpackting
result = { 0: 1.1181753789488595, 1: 0.5566080288678394, 
           2: 0.4718269778030734, 3: 0.48716683119447185, 
           4: 1.0, 5: 0.1395076201641266, 6: 0.20941558441558442 }
names = ['id','data']
formats = ['f8','f8']
dtype = dict(names = names, formats=formats)
input_array = np.array(list(result.items()), dtype=dtype)

# Show numpy data before any action
print('BEGINNING','-'*60)
print('\nRepresentation of the input data before any action:')
print(repr(input_array))
print('\nAbove data is serilized into json file.')

# json-serialization of the numpy array
content_to_json = jsonpickle.encode(input_array)

# putting json-serialized numpy array into json file
json_file_name = 'numpydata_in_file.json'
opened_json = io.open(json_file_name, 'w')
opened_json.write(content_to_json)
opened_json.close()

#reading json file to numpy_array_from_file
opened_json = io.open(json_file_name, 'r')
content_from_opened_json = opened_json.read()
numpy_array_from_file = jsonpickle.decode(content_from_opened_json)

# Show numpy data extracted from json file
print('\n\nRepresentation of deserilized data read from the json file.')
print(repr(numpy_array_from_file))

# compering input numpy array and numpy array2 read form json file
if (str(input_array) == str(numpy_array_from_file)):
    print('\nInput array is equal to array read from json file.')
else:
    print('\nInput array is NOT equal to array read from json file.')

print('\nEND','-'*60)