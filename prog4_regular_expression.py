import re

quote  = "I scream, you scream, we all scream for ice cream."

print(re.search("cream", quote))

print(re.findall("scream", quote))

print(re.split("you", quote))

text1 = "I have 2 apples and 3 oranges"

matches = re.findall(r'\d+', text1)
print(matches)

text2 = "The year is 2025"
matches = re.findall(r'\d{4}', text2)

# \D (Matches the non-digit character [^0-9])

text3 = "123 Main st."
match_str3 = re.findall(r'\D+', text3)
print(match_str3)

text4 = "House Number 45A"
match_str4 = re.findall(r'\D{3}', text2)
print(match_str4)

# \s (Matches any white spaces characters)
text5 = "Python  is awesome."
match_str5 = re.findall(r'\s{2}',text5) 
print(match_str5)

# \S (Matches any non-white spaces characters[^ \t\n\r\f\v])
text5 = "Hello World !  "
match_str5 = re.findall(r'\S+',text5) 
print(match_str5)

text6 = "abcde12345"
match_str6 = re.findall(r'\S{6}', text6) # checks nonwhite character of length 5
print(match_str6)

# \w (Matches alphanumeric character (a-zA-Z0-9))
text7 = "Hello123"
match_str7 = re.findall(r"\w+", text7)
print(match_str7)

text8 = "A1_B1"
match_str8 = re.findall(r"\w{2}", text8)
print(match_str8)

# \W (Matches any non-alphanumeric characters [^a-zA-Z0-9])
text9 = "Hello, World!"
match_str9 = re.findall(r"\W+", text9)
print(match_str9)

text10 = "Good!?"
match_str10 = re.findall(r"\W{2}", text10)
print(match_str10)


