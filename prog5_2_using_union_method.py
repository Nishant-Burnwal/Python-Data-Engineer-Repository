# PROG 5.2: Using the union() Method

# Define friend lists
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Using set union with union() method
all_friends = list(set(school_friends).union(college_friends))

print("All friends (Set union method):", all_friends)
