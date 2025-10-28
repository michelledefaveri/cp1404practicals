"""
Estimated time = 20 minutes
Actual Time = 27 minutes
"""

word_to_count = {}

# Ask user to enter a string
text = input("Text: ")
# Split string into individual words
words = text.split()
for word in words:
    # Get the current count of the word from the dictionary
    # If the word isn't in the dictionary, return 0
    frequency = word_to_count.get(word,0)
    # Count words
    word_to_count[word] = frequency + 1

# Find the length of the longest word for formatting
max_length = max((len(word) for word in words))

for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")