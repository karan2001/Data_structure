import array as arr
float_array=arr.array("d",[10.24,10.54,67.34,99.43])

float_array.append(42.67)

float_array.append(78.42)

float_array.remove(10.54)

print(float_array.index(67.34))

print(float_array)