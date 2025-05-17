# Implement bubble sort on a list of integers. Return the sorted list.

# Example:
# bubble_sort([5, 2, 9, 1]) → [1, 2, 5, 9]


def bubble_sort(l):

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            print(f"Comparing {l[i]}(i={i}) and {l[j]}(j={j})")

            if l[i] > l[j]:
                print(f"Swapping {l[i]}(i={i}) and {l[j]}(j={j})")
                print(f"Before: {l}")
                l[i], l[j] = l[j], l[i]
                print(f"After: {l}")
    
    print(l)

bubble_sort([5, 2, 9, 1])