school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Using set intersection with & operator
common_friends = list(set(school_friends) & set(college_friends))
print("Common friends (Set & operator):", common_friends)
