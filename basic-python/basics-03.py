events = [
    {"timestamp": "2023-05-01 08:00:00", "user": "alice"},
    {"timestamp": "2023-05-01 09:30:00", "user": "bob"},
    {"timestamp": "2023-05-01 10:00:00", "user": "alice"},
    {"timestamp": "2023-05-02 11:00:00", "user": "charlie"},
    {"timestamp": "2023-05-02 12:00:00", "user": "alice"}
]

# Expected output:
# {
#   '2023-05-01': 2,
#   '2023-05-02': 2
# }


# out_dates = {}

# for e in events:
#     if e["timestamp"] not in out_dates:
#         out_dates["timestamp"] = 0




# ------------------------------

# from collections import defaultdict # Nice short tutorial: https://www.freecodecamp.org/news/how-to-use-defaultdict-python/

# unique_users = defaultdict(set)

# for event in events:
#     date = event["timestamp"].split(" ")[0]
#     user = event["user"]
#     unique_users[date].add(user)

# # Convert to final format
# result = {date: len(users) for date, users in unique_users.items()}
# print(result)
    

