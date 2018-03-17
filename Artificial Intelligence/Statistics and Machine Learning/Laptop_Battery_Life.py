import fileinput

for line in fileinput.input():
    data=float(line)
    
if data>4:
    print("8")
else:
    print(2*data)
