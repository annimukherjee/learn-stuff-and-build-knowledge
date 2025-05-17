# Q1: Frequency Counter
# Write a function that takes a list of strings and returns a dictionary with the count of each string.

# Example input:
words = ["cat", "dog", "cat", "bird", "dog", "cat"]

# Expected output:
# {'cat': 3, 'dog': 2, 'bird': 1}

freq_dic = {}
for w in words:

    if w not in freq_dic:
        freq_dic[w] = 0

    freq_dic[w] += 1

print(freq_dic)


# ------ [improvement] ------

# from collections import Counter 
# freq_dic = Counter(words)