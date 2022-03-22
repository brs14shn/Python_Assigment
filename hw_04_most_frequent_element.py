

Let's take a list and try to find the most repeated number 
and how many times it repeats in the list.
Output=the most frequent number is 3 and it was 4 times repeated"
"""

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
most_common=max(numbers,key=numbers.count)
frequent_number=numbers.count(most_common)
print(f"The most frequent numbers is {most_common} and it was {frequent_number}times repeated.")
