# Example input:
raw_data = [
    "12,35",
    "bad line",
    "44,21",
    "error",
    "100,200"
]

# Expected output:
# [(12, 35), (44, 21), (100, 200)]

l = []

for line in raw_data:

    if "," not in line:
        continue
    elif "," in line and len(line.split(","))==2:
        l.append((int(line.split(",")[0]),int(line.split(",")[1]) ))

print(l)


# --------------------

# cleaned = []

# for line in raw_data:
#     try:
#         x_str, y_str = line.split(",")
#         cleaned.append((int(x_str), int(y_str)))
#     except:
#         continue