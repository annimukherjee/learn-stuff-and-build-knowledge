# 🛠️ Round 4: Mini Tool Logic

# Q4: Command-Line Timer Helper
# Write a Python function that simulates a simple timer. It should accept a number of seconds and print a countdown to 0, updating once per second.

import time
n = int(input("Enter number of seconds: "))

for i in range(n):
    print(n-(i))
    time.sleep(1)


# ----------------


# for i in range(n, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Time's up!")