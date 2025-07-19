school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Iterative common check
common_friends = []
for friend in school_friends:
    if friend in college_friends:
        common_friends.append(friend)

print("Common friends (Iterative method):", common_friends)
