# Input: [1, 3, 2, 2, 4], target = 4 → Output: (1,3), (2,2)
# Find All Pairs That Sum to a Target

list1 = [1, 3, 2, 2, 4]
target = int(input("Enter the target element: "))  # suppose 4
printed = set()

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] + list1[j] == target:
            pair = tuple(sorted((list1[i], list1[j])))
            if pair not in printed:
                print(pair)
                printed.add(pair)

