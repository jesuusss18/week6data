#I wrote print("Problem #") so when I run the code I can know the result that each problem is giving,

# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers :
        return None
    
    counted = {}
    
    for number in numbers:
        if number in counted:
            counted[number] += 1
        else:
            counted[number] = 1

    max_key = max(counted, key=counted.get)
    return max_key
print("Problem 1")


print(most_frequent([1, 2, 2, 3, 3, 3])) 
print(most_frequent([1,1,1,1,1,1,1])) 
print(most_frequent([])) 
print(most_frequent([1])) 
print(most_frequent(["a","b","c","d","a"])) 

"""
Time and Space Analysis for problem 1:

- Best-case:
  It is O(n), since we must count all elements regardless of early findings.

- Worst-case:
  O(n) time — we go through the entire list and update the dictionary for each element.

- Average-case:
  Also O(n), as each element requires a constant-time dictionary operation.

- Space complexity:
  O(n) — in the worst case (all elements unique), the dictionary stores n entries.

- Why this approach?
  A dictionary  provides constant-time inserts and lookups,
  making it efficient for frequency counting compared to using nested loops (which would be O(n^2)).

- Could it be optimized?
  Time complexity is already optimal at O(n). Space could only be reduced if we sorted the list,
  but that would increase time complexity to O(n log n), which is worse overall.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    ordered_list = []

    for num in nums:
        if num not in seen:
            ordered_list.append(num)
            seen.add(num)
        else:
            pass
    return ordered_list
print("Problem 2")

print(remove_duplicates([1,2,3,2,3,4,5]))
print(remove_duplicates([]))
print(remove_duplicates([1]))
print(remove_duplicates([1,1,1,1,1,1]))
print(remove_duplicates(["a","b","c","a"]))
print(remove_duplicates([1,-2,-3,-2]))

"""
Time and Space Analysis for problem 2:

- Best-case:
  Even if all elements are unique or all are duplicates, the loop still processes every element.
  So best-case time is still O(n).

- Worst-case:
  O(n) time — we loop through the list once, and checking/inserting in a set is O(1) on average.

- Average-case:
  Also O(n), since we always perform one pass through the list.

- Space complexity:
  O(n) — in the worst case, all elements are unique, so both 'seen' and 'ordered_list' store n items.

- Why this approach?
  Using a set gives constant-time lookups, making it efficient. It also preserves order naturally by only appending the first time each element appears.

- Could it be optimized?
  Time complexity is already optimal at O(n). Space could be reduced slightly using an ordered dictionary or using only one list, but fundamentally, you need extra storage to track seen elements, so O(n) space is unavoidable.
"""
"""
Performance and Space Analysis:

- Time Complexity:
  O(n) — Each element is checked exactly once, and set lookups/additions are O(1) on average.
  This is significantly faster than a naive nested loop approach, which would be O(n^2).

- Space Complexity:
  O(n) — We store all unique elements in 'seen' and the result in 'ordered_list'.
  Total extra space is proportional to the number of unique elements.

- Optimization Explanation:
  Compared to a naive approach that might check every element against the result list each time,
  using a set for 'seen' drastically reduces lookup time from O(n) per check to O(1) average-case,
  giving an overall O(n) solution instead of O(n^2).

- Further Notes:
  - Preserves the order of first occurrence.
  - Cannot be further optimized in time without changing the constraints.
"""

# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        number_needed = target - num
        if number_needed in seen:
            pairs.add(tuple(sorted((num,number_needed))))
        seen.add(num)
    return list(pairs)
print("Problem 3")

print(find_pairs([1,2,3,4,5],7))
print(find_pairs([2,8,2,3,7],10))
print(find_pairs([1,2,3],4))
print(find_pairs([-13,5,13,4,-5],10))
print(find_pairs([1,4,7],8))
print(find_pairs([],3))
print(find_pairs([13,-1,-2,3,14,-5],12))

"""
Time and Space Analysis for problem 3:

- Best-case :
  Even if valid pairs are found at the beginning, the loop must still iterate through the entire list,
  so runtime is still O(n). There is no early exit.

- Worst-case:
  O(n) time — because we go through every number once, and all set lookups/inserts are O(1) on average.

- Average-case:
  Also O(n), as we always iterate through all elements regardless of how many pairs are found.

- Space complexity:
  O(n) — in the worst case, all elements are stored in the 'seen' set. 
  The number of pairs stored in 'pairs' is at most O(n/2), which is still O(n).

- Why this approach?
  This approach uses a set for constant-time lookups, making it efficient.
  It avoids checking every pair manually (which would be O(n^2)), and ensures uniqueness with sorting + tuples.

- Could it be optimized?
  In terms of time complexity, this is already optimal at O(n).
  However, if the list were already sorted, we could use a two-pointer approach without extra space (O(1) space).
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n,initial_capacity = 4):
    my_list = []
    capacity = initial_capacity

    for i in range (1, n + 1):
        if len(my_list) == capacity:
            capacity *= 3
            print(f"Resizing to {capacity}")

        my_list.append(i)
        print(f"Added {i}: list size {len(my_list)}, capacity {capacity}")

    return my_list
print("Problem 4")
add_n_items(0)
add_n_items(10)
add_n_items(6)
add_n_items(4)
add_n_items(2)

"""
Time and Space Analysis for problem 4:

- When do resizes happen?
  Resizes happen whenever the number of elements in the list reaches the current capacity.
  At that point, the capacity is doubled and all existing elements are copied into a new larger list.

- What is the worst-case for a single append?
  The worst-case is O(n) when a resize occurs because every existing element must be copied to the new list.
  Most appends, however, are O(1) when there is still capacity.

- What is the amortized time per append overall?
  Amortized time is O(1) per append.  
  Even though some appends trigger expensive resizes, doubling ensures that these resizes happen infrequently enough
  that the average cost per append remains constant over many operations.

- Space complexity:
  O(n) — we need space for all n elements.  
  When a resize occurs, a temporary larger list is created, but the total extra space is proportional to n.

- Why does doubling reduce the cost overall?
  Doubling ensures that the number of resizes grows logarithmically with n.  
  Each resize copies many elements, but since the list size doubles, the number of copies per element averages out,
  keeping the **amortized cost of each append constant**.
"""



# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)
    return result
print("Problem 5")

print(running_total([1,2,3,4]))
print(running_total([]))
print(running_total([1,1,1,1,1,1]))
print(running_total([1,-2,-3]))
print(running_total([2,2,2,2,2,2,2]))

"""
Time and Space Analysis for Problem 5:

- Best-case:
  O(n) — we have to iterate through all elements regardless of values.

- Worst-case:
  O(n) — same reasoning, one pass through the list.

- Average-case:
  O(n) — each element is processed once.

- Space complexity:
  O(n) — we create a new list of the same size as the input to store the running totals.

- Why this approach?
  It is simple, clear, and efficient. By keeping a running total variable, we avoid nested loops.

- Could it be optimized?
  Time complexity is already optimal. Space could be reduced if we modify the input list in place, 
  but creating a new list is usually safer to avoid side effects.
"""

