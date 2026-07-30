import os
with open("practice.txt") as f:
     content=f.read()
with open("rename_practice.txt","w") as f:
     f.write(content)
os.remove("practice.txt")