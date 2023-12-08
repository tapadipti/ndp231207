import numpy
n = 9
data = ["Dummy data "] * n * 100000
with open('new-file.txt', 'w') as f: f.writelines(data)