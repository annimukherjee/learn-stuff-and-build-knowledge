
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
# [1, 4, 9]

nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4]

squared_lst_comp = [x**2 for x in nums]         # map
evens_lst_comp = [x for x in nums if x % 2==0]  # filter


print(nums)
print(squared)

print(squared_lst_comp)
print(evens_lst_comp)
