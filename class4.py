# Python Lists

"""
 In Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, Python lists are very flexible:
"""

"""
# Can contain duplicate items
# Mutable: items can be modified, replaced, or removed
# Ordered: maintains the order in which items are added
# Index-based: items are accessed using their position (starting from 0)
# Can store mixed data types (integers, strings, booleans, even other lists)
"""

# Creating a List
"""
Lists can be created in several ways, such as using square brackets, the list() constructor or by repeating elements. Let's look at each method one by one with example:
"""

# list = [1, 2, 3, 4, 5]


# print(type(list))  
# print(len(list))
# print("Original List:", list)
# print("First Element:",list[0])  # accessing first element
# print("Last Element:",list[-1])   # accessing last element
# print(list[0:3])  # slicing the list from index 0 to 2
# print("List Repeated:", list * 2)  # repeating the list



list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "kiwi", "melon"]



# newlist = list1 + list2
# print("Concatenated List:", newlist)


# a = list((1, 2, 3, 'apple', 4.5))  
# print(a)

# b = list("hello")




# a = [2] * 5
# b = [0] * 7

# print(a)
# print(b)

# list = [1,1,"hello",1.4]

# list[1] = 2

# print(list)

# tuple = (1,2,3,3)
# print(type(tuple))
# print(tuple)

# changetolist = list(tuple)
# print(changetolist)
# print(type(changetolist))

# set = {1,2,3}
# print(type(set))
# print(set)

# change = list(set)
# print(type(change))
# print(change)

# str = "hasnain"

# strtolist = list(str)
# print(strtolist)

# list = [1,2]

# dublelist = list * 3

# print(dublelist)

# list = ["a","b","c"]

# list.append("d")
# list.extend(["d","e","f","g"])
# list.insert(1,"z")
# list.remove("b")
# list.clear()
# list.sort()


# print(list)


# nested_list = [1, 2, [3, 4], [5, 6]]
# print(nested_list[2] [0])        # Output: [3, 4]

# list = [5, 2, 9, 1, 5, 6]
# # list[2] = 3

# print(list)

# li = ['a', 'b', 'c', 'd', 'e'] 
# print(li[0:3] )
