# Example input:
logs = [
    "[2023-03-14 10:12:45] user123: clicked button",
    "[2023-03-14 10:13:02] user456: scrolled down",
    "[2023-03-14 10:13:07] user123: submitted form"
]

# Expected output:
# [
#   {"timestamp": "2023-03-14 10:12:45", "user": "user123", "action": "clicked button"},
#   {"timestamp": "2023-03-14 10:13:02", "user": "user456", "action": "scrolled down"},
#   {"timestamp": "2023-03-14 10:13:07", "user": "user123", "action": "submitted form"}
# ]

cleaned_logs = []
for log in logs:
    l = log.split(" ")
    # print(l)
    d = {"timestamp": "", "user": "", "action": ""}
    d["timestamp"] = l[0]+ " " + l[1]
    d["timestamp"]= d["timestamp"][1:-1]

    d["user"] = l[2][:-1]

    d['action'] = l[-2] + " " + l[-1]

    cleaned_logs.append(d)

for c_l in cleaned_logs:
    print(f"{c_l}")


# ---------------------

cleaned_logs = []

# for log in logs:
#     timestamp_part, rest = log.split("] ")
#     timestamp = timestamp_part[1:]
#     user, action = rest.split(": ", 1) 
#                                           # Looks for the pattern ": " in the string
#                                           # Splits the string at the FIRST occurrence only (that's what the 1 parameter means)
#     cleaned_logs.append({"timestamp": timestamp, "user": user, "action": action})