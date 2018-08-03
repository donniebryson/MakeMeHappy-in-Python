import math
import json
print("This is just me playing around")
year = 2016; event = 'refrendum'
print(f'Results of the {year} {event}')
print(f'Pi is {math.pi: .6f}')
my_var = [1, "simple", "list"]
with open('text.txt', 'w') as myFile:
    # myFile.write("I want to read this line")
    json.dump(my_var, myFile)


