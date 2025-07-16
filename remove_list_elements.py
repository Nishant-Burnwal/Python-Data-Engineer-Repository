# PROG 4: remove some elements from the list
colors = ["Red", "Green", "Pink", "Blue", "Black", "Purple", "Yellow", "Magenta", "Brown"]

print(f"Colors List: {colors}\n")

indices_to_remove = [0, 2, 3]
revised_colors = []

for index, color in enumerate(colors):
    if index not in indices_to_remove:
        revised_colors.append(color)

print(revised_colors)