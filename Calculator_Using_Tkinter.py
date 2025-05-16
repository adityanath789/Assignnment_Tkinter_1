# Get message from user
message = input("Enter a message: ")

# Dictionary to store character frequencies
char_freq = {}

# Count frequency of each character
for char in message:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Display the results
print("\nCharacter Frequencies:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")