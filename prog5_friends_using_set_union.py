school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Using | operator
all_friends_pipe = list(set(school_friends) | set(college_friends))
print("All friends (Set | operator):", all_friends_pipe)

# Using union() method
all_friends_union = list(set(school_friends).union(college_friends))
print("All friends (Set union method):", all_friends_union)
