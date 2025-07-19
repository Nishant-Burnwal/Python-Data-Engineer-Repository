# PROG 5.1: Using the | Operator

# Define friend lists
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Using set union with | operator
all_friends = list(set(school_friends) | set(college_friends))

print("All friends (Set | operator):", all_friends)
