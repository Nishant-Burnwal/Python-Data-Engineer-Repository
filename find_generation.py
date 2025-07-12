# Find Generation

# Enter the birth year
birth_year = int(input('Enter Birth Year: '))

# Print the generation using Python shorthand conditions
print(
    f'Birth Year: {birth_year}',
    f'Baby Boomer: {birth_year >= 1946 and birth_year < 1964}',
    f'Gen X: {birth_year >= 1965 and birth_year < 1980}',
    f'Millennial: {birth_year >= 1981 and birth_year < 1996}',
    f'Gen Z: {birth_year >= 1997 and birth_year < 2013}',
    f'Gen Alpha: {birth_year >= 2013 and birth_year < 2035}',
    sep='\n'
)
