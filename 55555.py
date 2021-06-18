import csv
import turtle as t

with open("new.txt", 'r') as f:
    lines = f.readlines()
    values = list(map(int, lines))
    print(values)

t.shape('turtle')
size = len(values)

for i in range(0, size - 1, 2):
    t.forward(values[i])
    t.right(values[i+1])
