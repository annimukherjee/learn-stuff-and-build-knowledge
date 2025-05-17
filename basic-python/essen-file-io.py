import pdb; 

with open('myfile.txt', 'r') as f:
    contents = f.read()
    print(contents)
print("-"*20)
print("Writing into the file now: ")
with open('myfile.txt', 'a') as f:
    f.write("\n\nHello, world!")

print("-"*20)

with open('myfile.txt', 'r') as f:
    contents = f.read()
    print(contents)

pdb.set_trace()

print("-"*20)
print("Reading line by line from the file now: ")
with open('myfile.txt', 'r') as f:
    i=0
    for line in f:
        i+=1
        print(f"{i}: {line.strip()}")