# Character Category Counter

text = input("Enter text: ")

uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0
other_count = 0

for character in text:

    if character.isupper():
        uppercase_count += 1

    elif character.islower():
        lowercase_count += 1

    elif character.isdigit():
        digit_count += 1

    elif character == " ":
        space_count += 1

    else:
        other_count += 1

print("\n----- Character Analysis -----")
print("Uppercase Letters:", uppercase_count)
print("Lowercase Letters:", lowercase_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Other Characters:", other_count)