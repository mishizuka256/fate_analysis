path = "setsuiribi.csv"
with open(path, "r")as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip("\n")
    if line == "":
        continue
    for ch in line:
        print(ch)
