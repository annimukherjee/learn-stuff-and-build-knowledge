# Is Palindrome

# Write a function to check if a string is a palindrome (same forwards and backwards), ignoring case and spaces.

s = input("Enter a string: ")
print(f"Before: {s}")
s = s.lower()
print(f"After: {s}")

if s==s[::-1]:
    print("Yes, it is a palindrome")
else:
    print("No it's not a palindrome")


# madam, raceCaR, mAaM